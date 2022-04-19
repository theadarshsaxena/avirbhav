from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('events/', views.events, name="events"),
    path('thanks', views.thanks, name='thanks'),
    path('events/<slug:slug>', views.event_detail, name="event_detail"),
    path('scores/', views.scores, name="scores"),
    path('sponsorus', views.sponsorus, name="sponsorus"),
    path('feedback', views.feedback, name="feedback"),
]