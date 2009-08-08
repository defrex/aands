from django.conf.urls.defaults import *

urlpatterns = patterns('categories.views',
		url(r'^(?P<categoryid>\d+)/', 'items_in_cat', name='cat_index'),
	#	url(r'^(?P<tag>.+)/$', 'tag_app.views.tags', name='tag_results'),
	)
