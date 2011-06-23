import random
from django.db import models

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

    def person_has_entered(self, person):
        if person in entrants or person in alternates:
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
    class Meta:
        model = Entrant
