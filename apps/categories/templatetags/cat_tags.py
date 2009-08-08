from django.template import Library
from django.core.urlresolvers import reverse
from categories.models import Category

register = Library()

@register.simple_tag
def category_select(current_GET):
	cats = Category.objects.all()
	output = '<select name="category" onchange="$(this).parent(\'form\').submit()">'
	output += '<option value="">All Categories</option>'
	for cat in cats:
		output += '<option value="'+cat.name+'"'
		if 'category' in current_GET:
			if cat.name == current_GET['category']:
				output += ' selected="selected"'
		output += '>'+cat.name+'</option>'
	output += '</select>'
	return output

@register.simple_tag
def category_list(current_GET):
	cats = Category.objects.all()
	output = ''
	for cat in cats:
		output += '<li'
		if 'category' in current_GET:
			if cat.name == current_GET['category']:
				output += ' class="current"'
		output += '><a href="/cat/'+str(cat.id)+'">'+cat.name+'</a></li>'
	return output
