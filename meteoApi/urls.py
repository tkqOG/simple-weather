from django.urls import path

from meteoApi import views

urlpatterns = [
    path("meteoApi/", views.local_temp, name="local_temp"),
    path("meteoApi/discover", views.random_location_temp, name="random_location_temp")
]
