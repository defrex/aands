from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
	name = models.CharField(max_length=100)
	
	def get_absolute_url(self):
		return reverse('cat_index', category=self.name)
	
	def __unicode__(self):
		return self.name
