from django.contrib import admin
from .models import RestaurantRating
class RestaurantRatingAdmin(admin.ModelAdmin):
	list_display = ['name', 'ecoRating']
admin.site.register(RestaurantRating, RestaurantRatingAdmin)