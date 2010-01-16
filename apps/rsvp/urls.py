
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^$', 'rsvp.views.main', name='rsvp'),
    url('^browse/$', 'rsvp.views.browse', name='rsvp_browse'),
)

