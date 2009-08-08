from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.template import RequestContext

from login.utils import render_login
from items.models import Item, Claim

def items(request, new=None):
    items = Item.objects.order_by('date_added')
    if new:
        items = items.extra(
            where=['(select count(*) from items_claim where items_item.id = items_claim.item_id) = 0'])
    
    return render_to_response("items/items.html", {"items": items}, 
            context_instance=RequestContext(request))
    
def new_items(request):
    items = Item.object.order_by('date_added')

    return render_to_response("items/items.html", {"items": items}, 
            context_instance=RequestContext(request))

def item(request, key):
    item = get_object_or_404(Item, pk=key)
    
    return render_to_response("items/view.html", {"item": item}, 
            context_instance=RequestContext(request))

def claim(request, key):
    resp = dict()
    if not request.user.is_authenticated():
        resp['status'] = 'ANON_USER'
        if request.method == 'POST':
            pass
        else:
            resp['output'] = render_login(request)

        return HttpResponse(simplejson.dumps(resp))
    item = get_object_or_404(Item, pk=key)
    claim, is_new = Claim.objects.get_or_create(user=request.user, item=item)
    if not is_new:
        claim.delete()
        resp['status'] = 'DELETED'
    else:
        claim.save()
        resp['status'] = 'CREATED'
    return HttpResponse(simplejson.dumps(resp))
    
