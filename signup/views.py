import random

from django import forms
from django.core import serializers
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

POD_COUNTS = [1, 2, 4, 8, 16, 32, 64, 128]

def home(request):
    tourneys = Tourney.objects.filter(active=True).order_by('start_time')
    return render_to_response('index.html', RequestContext(request,{'tourneys': tourneys}))

def signup(request, pk):
    tourney = Tourney.objects.get(pk=pk)
    if request.method == 'POST':
        form = EntrantForm(request.POST)
        if form.is_valid():
            entrant = form.save()
            tourney.entrants.add(entrant)
            return HttpResponseRedirect('/success/' + tourney.id.__str__())
    else:
        form = EntrantForm()
    return render_to_response('tourney.html', RequestContext(request,{'tourney': tourney, 'form': form}))

def signup_success(request, pk):
    return render_to_response('signup-success.html', RequestContext(request, {'pk': pk}))

def get_tourney(request, pk):    
    tourney = Tourney.objects.get(pk=pk)
    return render_to_response('list.html', RequestContext(request,{'tourney': tourney}))

def get_bracket(request, pk):
	pass
#    tourney = Tourney.objects.get(pk=pk)
#    max = tourney.entrants.aggregate(Max('wins'))
#    max =  max['wins__max']
#    
#    participants = tourney.get_entrants()
#    alternates = tourney.get_alternates()
#   
#    p_list = []
#    for p in participants:
#    	person = {'id': p.id, 'name': p.name}
#    	p_list.append(person)
#    	
#    random.shuffle(p_list)
#    	
#    return render_to_response('bracket.html', RequestContext(request,{'tourney': tourney, 'participants': p_list, 'alternates': alternates}))
    
#def build_round(request, pk, index, max_entrants):
#    tourney = Tourney.objects.get(pk=pk)
#    round = new Round(index=index, tourney=tourney, max_per_pod=max_entrants)
#    
    #build pods
        #get max win number from entrants list
        #get list of entrants with that win count
        #get nearest larger number in POD_COUNTS
    	#create pods
    	#assign one entrant per pod, iterate till done (no empty pods)