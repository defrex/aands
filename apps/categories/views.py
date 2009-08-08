from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from categories.models import Category
from items.models import Item

def items_in_cat(request, categoryid):
	cat = get_object_or_404(Category, id=categoryid)
	items = Item.objects.filter(category=cat)
	
	return render_to_response('items/items.html', {
		'category': cat,
		'items': items,
	}, RequestContext(request))
