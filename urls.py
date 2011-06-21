from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView

from signup.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signup.views.home', name='home'),

    url(r'^tourney/(?P<pk>\d+)/$', 'signup.views.signup'),
    url(r'^list/(?P<pk>\d+)/$', 'signup.views.get_tourney'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
