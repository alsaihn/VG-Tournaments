from django.db import models

# Create your models here.

class Entrant(models.Model):
    name = models.CharField(max_length=255)
    badge_number = models.IntegerField()

    def __unicode__(self):
        return self.name


class Tourney(models.Model):
    name = models.CharField(max_length=255)
    rules = models.TextField()
    cutoff = models.IntegerField()
    has_alternate_list = models.BooleanField(default=True)

    entrants = models.ManyToManyField(Entrant, related_name='entrants', blank=True, null=True)
    alternates = models.ManyToManyField(Entrant, related_name='alternates', blank=True, null=True)

    def person_has_entered(self, person):
        if person in entrants or person in alternates:
            return True;
        return False;

    def __unicode__(self):
        return self.name
