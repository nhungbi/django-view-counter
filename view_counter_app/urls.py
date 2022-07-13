
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.track_view)
]