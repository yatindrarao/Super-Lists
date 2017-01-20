from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey('List', default='')

class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])
