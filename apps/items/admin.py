from django.contrib import admin
from items.models import Item
from items.forms import ItemAdminModelForm

class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminModelForm

admin.site.register(Item, ItemAdmin)
