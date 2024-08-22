from django.urls import path
from . import views

urlpatterns = [
    path("myStravaApp", views.index, name="index"),
]
