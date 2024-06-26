from django.urls import path

from . import views

app_name = 'firstapp'

urlpatterns = [
    path("", views.AlbumView, name = "index")
]
