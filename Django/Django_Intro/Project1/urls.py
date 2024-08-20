from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name='greet'),
    path("Asyikin", views.Asyikin, name="Asyikin"),
    path("Guests", views.Guests, name='Guests')
]

