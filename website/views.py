from django.shortcuts import render
import requests
import json
from .models import *
# Create your views here.
def home(request):
	return(render(request, 'home.html'))
def about(request):
	return(render(request, 'about.html'))
def goal(request):
	return(render(request, 'goal.html'))
def importance(request):
	return(render(request, 'importance.html'))

def carbon(request, ip=None, location=None):
	if(ip == None):
		return(render(request, 'carbon.html'))
	if(location == None):
		ip_json = requests.get('http://api.ipify.org?format=json')
		ip = json.loads(ip_json.text)
		res = requests.get('http://ip-api.com/json/'+ip["ip"])
		location_info = res.text
		location = json.loads(location_info)
		#location = (location_info["lat"], location["lon"])
		#return(render(request, 'info.html', {"data": location}))
	print(location["lat"], location["lon"])
	url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="+str(int(location["lat"]))+"%2C"+str(int(location["lon"]))+"&radius=5000&type=restaurant&key=AIzaSyCwCSjxySYwxjWsHrErgfd0PSFAd3mcrz4"
	payload={}
	headers = {}
	response = requests.request("GET", url, headers=headers, data=payload)
	res = response.text;
	dic = json.loads(res)
	names = []
	ecoRatings = []
	qualityRatings = []
	currentlyOpen = []
	photoKeys = []
	for restaurant in dic["results"]:
		rests = RestaurantRating.objects.all()
		for r in rests:
			if(r.name == restaurant["name"]):
				print("HERE")
				names.append(restaurant["name"])
				ecoRatings.append(r.ecoRating)
				qualityRatings.append(int(restaurant["rating"]))
				if(restaurant["opening_hours"]["open_now"] == True):
					currentlyOpen.append("Yes")
				else:
					currentlyOpen.append("No")
				photoKeys.append(restaurant["photos"][0]["photo_reference"])
				photoKeys[-1] = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference="+str(photoKeys[-1])+"&key=AIzaSyCwCSjxySYwxjWsHrErgfd0PSFAd3mcrz4"

	l = zip(names, ecoRatings, qualityRatings, currentlyOpen, photoKeys)
	#for i in l:
	#	print(i)


	return(render(request, 'info.html', {"l": l}))