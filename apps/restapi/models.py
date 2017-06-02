# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Track(models.Model):
	name = models.CharField(max_length=255)
	artist = models.CharField(max_length=255)
	# album = models.CharField(max_length=255)
	spotify_id = models.CharField(max_length=255)
	# href = models.URLField()
	uri = models.CharField(max_length=255)
	# imageURL = models.URLField()

class User(models.Model):
	display_name = models.CharField(max_length=255)
	# email = models.EmailField(max_length=255)
	spotify_id = models.CharField(max_length=255)
	active_track = models.ForeignKey(Track, related_name="users", null=True)
	# track_added = models.DateTimeField()
	following = models.ManyToManyField("self", related_name="followers", symmetrical=False, blank=True)
	# href = models.URLField()
	# uri = models.CharField(max_length=255)
	# imageURL = models.URLField()