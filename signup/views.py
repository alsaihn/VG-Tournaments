import random

from django.core import serializers
from django.db.models import Max
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def home(request):
    tourneys = Tourney.objects.all()
    return render_to_response('index.html', RequestContext(request,{'tourneys': tourneys}))

def signup(request, pk):
    tourney = Tourney.objects.get(pk=pk)
    if request.method == 'POST':
        form = EntrantForm(request.POST)
        if form.is_valid():
            entrant = form.save()
            tourney.entrants.add(entrant)
            return HttpResponseRedirect('/list/' + pk.__str__())
    else:
        form = EntrantForm()
    return render_to_response('tourney.html', RequestContext(request,{'tourney': tourney, 'form': form}))

def get_tourney(request, pk):    
    tourney = Tourney.objects.get(pk=pk)
    return render_to_response('list.html', RequestContext(request,{'tourney': tourney}))

def get_bracket(request, pk):
    tourney = Tourney.objects.get(pk=pk)
    max = tourney.entrants.aggregate(Max('wins'))
    max =  max['wins__max']
    
    participants = tourney.entrants.all()[:tourney.cutoff]
    alternates = tourney.entrants.all()[tourney.cutoff:]
   
    p_list = []
    for p in participants:
    	person = {'id': p.id, 'name': p.name}
    	p_list.append(person)
    	
    return render_to_response('bracket.html', RequestContext(request,{'tourney': tourney, 'participants': p_list, 'alternates': alternates}))