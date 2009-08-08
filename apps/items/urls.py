from django.conf.urls.defaults import *

urlpatterns = patterns('items.views',
    url(r'^$', 'items', name='items'),
    url(r'^unregistered/$', 'items',{'new': True}, name='items_unreged'),
    url(r'^(\d+)/claim/$', 'claim', name='items_claim'),
    url(r'^(\d+)/$', 'item', name='items_item'),
)


