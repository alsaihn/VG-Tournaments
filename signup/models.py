import random
from django.db import models
from django import forms


# Create your models here.

class Entrant(models.Model):
    name = models.CharField(max_length=255)
    badge_number = models.IntegerField()
    registered_on = models.DateTimeField(auto_now_add=True, editable=False)
    wins = models.IntegerField(default=0, editable=False)

    def __unicode__(self):
        return self.name


class Tourney(models.Model):
    name = models.CharField(max_length=255)
    rules = models.TextField()
    cutoff = models.IntegerField()
    has_alternate_list = models.BooleanField(default=True)

    entrants = models.ManyToManyField(Entrant, related_name='entrants', blank=True, null=True)

    def person_has_entered(self, name, badge):
    	for e in self.entrants.all():
    	    if e.name == name or e.badge_number == badge:
        	return True;
        return False;

    def get_entrants(self):
        return random.shuffle(self.entrants.all[:64])

    def get_alternates(self):
        return self.entrants.all[64:]

    def __unicode__(self):
        return self.name

from django.forms import ModelForm

class EntrantForm(ModelForm):
    tourney_pk = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Entrant
        
    def clean(self):
    	cleaned_data = self.cleaned_data
	name = cleaned_data.get('name')
	badge_number = cleaned_data.get('badge_number')
	tourney_pk = cleaned_data.get('tourney_pk')

	tourney = Tourney.objects.get(pk=tourney_pk)
	if tourney.person_has_entered(name, badge_number):
	    raise forms.ValidationError("Name or badge_number has already entered!")

	return cleaned_data
	