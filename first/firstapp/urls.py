from django.urls import path

from . import views

app_name = 'firstapp'

urlpatterns = [
    path("", views.HomeView.as_view(), name = "index"),
    path("album/<int:id>/", views.AlbumView.as_view(), name = "album_detail")
    
]
