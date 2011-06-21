from django.core import serializers
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

