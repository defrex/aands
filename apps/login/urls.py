from django.conf.urls.defaults import *

urlpatterns = patterns('login.views',
    url(r'^$', 'handle_login', name='login_handle_login'),
    url(r'^form/$', 'login_form', name='login_form'),
)


