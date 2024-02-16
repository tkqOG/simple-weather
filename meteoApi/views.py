from datetime import datetime

import geocoder as geocoder
import requests

from django.http import HttpResponse
from django.template import loader

from meteoApi.models import WorldCities


def random_location_temp(request):
    random_item = WorldCities.objects.all().order_by('?').first()
    city = random_item.city
    location = [random_item.lat, random_item.lng]
    temp = get_temp(location)
    template = loader.get_template('index.html')
    context = {
        'city': city,
        'temp': temp,
    }
    return HttpResponse(template.render(context, request))


def local_temp(request):
    location = geocoder.ip('me').latlng
    temp = get_temp(location)
    template = loader.get_template('index.html')
    context = {
        'city': "Your Location",
        'temp': temp,
    }
    return HttpResponse(template.render(context, request))


def get_temp(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    weather_data = requests.get(api_request).json()
    temp = weather_data['hourly']['temperature_2m'][hour]
    return temp
