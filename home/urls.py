from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('events/', views.events, name="events"),
    path('thanks', views.thanks, name='thanks'),
]