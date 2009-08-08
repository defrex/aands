from django.template import Library
from items.models import Claim

register = Library()

@register.inclusion_tag("items/item.html", takes_context=True)
def show_item(context):
    return {'item': context['item'],'request': context['request'],
            'MEDIA_URL': context['MEDIA_URL']}

@register.filter
def has_claimed(user, item):
    "returns true if the user has claimed the item"
    if not user.is_authenticated():
        return False
    claim_exists = Claim.objects.filter(user=user, item=item).count()
    if claim_exists:
        return True
    else:
        return False
