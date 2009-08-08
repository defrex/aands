from django import forms
#from tinymce.widgets import TinyMCE
from items.models import Item

class ItemAdminModelForm(forms.ModelForm):
    #description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 15}))

    class Meta:
        model = Item
