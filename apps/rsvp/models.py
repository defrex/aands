
from django.db import models
from django.utils.safestring import mark_safe

MEAL_CHOICES = (
    ('reg', u'<strong>Regular</strong><p>Blerb about regular dish</p>'),
    ('veg', u'<strong>Vegitarian</strong><p>blerb about vegi dish</p>'),
    ('kid', u'<strong>Kids</strong><p><em>For ages 1-6 only.</em><br />kids food blerb</p>'),
)

class RSVP(models.Model):
    name = models.CharField(max_length=255)
    meal_options = models.CharField(max_length=3, choices=MEAL_CHOICES, default=MEAL_CHOICES[0])



