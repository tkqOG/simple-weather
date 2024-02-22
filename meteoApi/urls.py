from django.urls import path

from meteoApi import views

urlpatterns = [
    path("simple-weather/", views.local_temp, name="local_temp"),
    path("simple-weather/discover", views.random_location_temp, name="random_location_temp")
]
