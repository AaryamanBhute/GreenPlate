from django.db import models

# Create your models here.
class RestaurantRating(models.Model):
	name = models.CharField(max_length=100)
	ecoRating = models.CharField(max_length=100)