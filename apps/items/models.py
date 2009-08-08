import Image

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from categories.models import Category

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True)
    picture = models.ImageField(upload_to="itemimages", blank=True, null=True)
    date_added = models.DateField(auto_now=True)
    category = models.ForeignKey(Category)

    def claimed(self):
        "returns 1 if the item is claimed, and 0 if not. A useful boolean."
        return Claim.objects.filter(item=self).count()

    def claimed_by(self, user):
        "returns 1 if the item is claimed by the user, and 0 if not."
        return Claim.objects.filter(item=self, user=user).count()

    def get_absolute_url(self):
        return reverse('item', key=self.pk)
    
    def save(self):
        super(Item, self).save()
        if self.picture:
            filename = self.picture.path
            image = Image.open(filename)
            
            image.thumbnail((300,200), Image.ANTIALIAS)
            image.save(filename)
    
    def __unicode__(self):
        return self.name

class Claim(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)


