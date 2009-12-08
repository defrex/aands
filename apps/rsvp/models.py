
from django.db import models
from django.utils.safestring import mark_safe

MEAL_CHOICES = (
    ('reg', u'<strong>Chicken</strong>'),
    ('veg', u'<strong>Vegetarian</strong>'),
    ('kid', u'<strong>Kids</strong> (<em>For ages 1-6 only.</em>)'),
)

ATT_CHOICES = (
    ('true', u'Yes'),
    ('false', u'No'),
)

class RSVP(models.Model):
    name = models.CharField(max_length=255)
    attending = models.BooleanField(choices=ATT_CHOICES, default=ATT_CHOICES[1])
    meal_options = models.CharField(max_length=3, choices=MEAL_CHOICES, default=MEAL_CHOICES[0])
    
    def __unicode__(self):
        return self.name



