from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def home(request):
    tourneys = Tourney.objects.all()
    return render_to_response('index.html', RequestContext(request,{'tourneys': tourneys}))

def get_tourney(request, pk):
    tourney = Tourney.objects.get(pk=pk)
    return render_to_response('tourney.html', RequestContext(request,{'tourney': tourney}))

