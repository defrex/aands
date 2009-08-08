from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    
    (r'^items/', include('items.urls')),
    (r'^cat/', include('categories.urls')),
    (r'^login/', include('login.urls')),
    
    url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'login/logout.html'}, name='login_logout'),
        
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
                {'document_root': settings.MEDIA_ROOT}),

    (r'^admin/', include(admin.site.urls)),
)

