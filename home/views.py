from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from home.models import Event, Scores

# Create your views here.
def index(request):
    context = {
        'scores': Scores.objects.first()
    }
    return render(request, "index.html", context)

def events(request):
    context = {
        'upcoming': Event.objects.filter(status='U'),
        'ongoing': Event.objects.filter(status='O'),
        'completed': Event.objects.filter(status='C'),
        'scores': Scores.objects.first()
    }
    return render(request, "events.html", context)

def thanks(request):
    return render(request, "feedback.html")