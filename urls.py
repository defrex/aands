from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    (r'^rsvp/', include('rsvp.urls')),
    url(r'^registration/$', direct_to_template, {'template': 'core/reg.html'}, name='reg'),
    url(r'^accomodations/$', direct_to_template, {'template': 'core/acom.html'}, name='acom'),
    url(r'^location/$', direct_to_template, {'template': 'core/loc.html'}, name='loc'),
    
    #(r'^items/', include('items.urls')),
    #(r'^cat/', include('categories.urls')),
    #(r'^login/', include('login.urls')),
    
    #url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'login/logout.html'}, name='login_logout'),
        
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
                {'document_root': settings.MEDIA_ROOT}),

    (r'^admin/', include(admin.site.urls)),
)

