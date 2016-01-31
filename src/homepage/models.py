from __future__ import unicode_literals

from django.db import models

# Create your models here.

class blog(models.Model):
	"""docstring for blog"""
	title = models.CharField(max_length = 100)
	context = models.TextField()
	after = models.DateTimeField()
	initial = models.DateTimeField()

	def __unicode__(self):
		return self.title
		