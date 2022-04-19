from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from home.models import Event, Scores

# Create your views here.
def index(request):
    h=0
    s=0
    g=0
    r=0
    events = Event.objects.filter(status='C')
    for event in events:
        if(str(event.winner)=="Hufflepuff"):
            h=h+event.winnerscore
        elif(str(event.winner)=="Slytherin"):
            s=s+event.winnerscore
        elif(str(event.winner)=="Gryffindor"):
            g=g+event.winnerscore
        elif(str(event.winner)=="Ravenclaw"):
            r=r+event.winnerscore
        if(str(event.firstrunner)=="Hufflepuff"):
            h=h+event.firstrunnerscore
        elif(str(event.firstrunner)=="Slytherin"):
            s=s+event.firstrunnerscore
        elif(str(event.firstrunner)=="Gryffindor"):
            g=g+event.firstrunnerscore
        elif(str(event.firstrunner)=="Ravenclaw"):
            r=r+event.firstrunnerscore
        if(str(event.secondrunner)=="Hufflepuff"):
            h=h+event.secondrunnerscore
        elif(str(event.secondrunner)=="Slytherin"):
            s=s+event.secondrunnerscore
        elif(str(event.secondrunner)=="Gryffindor"):
            g=g+event.secondrunnerscore
        elif(str(event.secondrunner)=="Ravenclaw"):
            r=r+event.secondrunnerscore
        if(str(event.thirdrunner)=="Hufflepuff"):
            h=h+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Slytherin"):
            s=s+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Gryffindor"):
            g=g+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Ravenclaw"):
            r=r+event.thirdrunnerscore
    context = {
        'h' : h,
        's' : s,
        'g' : g,
        'r' : r,
    }
    return render(request, "index.html", context)

def events(request):
    h=0
    s=0
    g=0
    r=0
    events = Event.objects.filter(status='C')
    for event in events:
        if(str(event.winner)=="Hufflepuff"):
            h=h+event.winnerscore
        elif(str(event.winner)=="Slytherin"):
            s=s+event.winnerscore
        elif(str(event.winner)=="Gryffindor"):
            g=g+event.winnerscore
        elif(str(event.winner)=="Ravenclaw"):
            r=r+event.winnerscore
        if(str(event.firstrunner)=="Hufflepuff"):
            h=h+event.firstrunnerscore
        elif(str(event.firstrunner)=="Slytherin"):
            s=s+event.firstrunnerscore
        elif(str(event.firstrunner)=="Gryffindor"):
            g=g+event.firstrunnerscore
        elif(str(event.firstrunner)=="Ravenclaw"):
            r=r+event.firstrunnerscore
        if(str(event.secondrunner)=="Hufflepuff"):
            h=h+event.secondrunnerscore
        elif(str(event.secondrunner)=="Slytherin"):
            s=s+event.secondrunnerscore
        elif(str(event.secondrunner)=="Gryffindor"):
            g=g+event.secondrunnerscore
        elif(str(event.secondrunner)=="Ravenclaw"):
            r=r+event.secondrunnerscore
        if(str(event.thirdrunner)=="Hufflepuff"):
            h=h+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Slytherin"):
            s=s+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Gryffindor"):
            g=g+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Ravenclaw"):
            r=r+event.thirdrunnerscore
    context = {
        'h' : h,
        's' : s,
        'g' : g,
        'r' : r,
        'upcoming': Event.objects.filter(status='U'),
        'ongoing': Event.objects.filter(status='O'),
        'completed': Event.objects.filter(status='C'),
    }
    return render(request, "events.html", context)

def thanks(request):
    return render(request, "feedback.html")

def event_detail(request, slug):
    event = Event.objects.get(slug=slug)
    context = {
        'event': event,
    }
    return render(request, "event-detail.html", context)

def scores(request):
    h=0
    s=0
    g=0
    r=0
    events = Event.objects.filter(status='C')
    for event in events:
        if(str(event.winner)=="Hufflepuff"):
            h=h+event.winnerscore
        elif(str(event.winner)=="Slytherin"):
            s=s+event.winnerscore
        elif(str(event.winner)=="Gryffindor"):
            g=g+event.winnerscore
        elif(str(event.winner)=="Ravenclaw"):
            r=r+event.winnerscore
        if(str(event.firstrunner)=="Hufflepuff"):
            h=h+event.firstrunnerscore
        elif(str(event.firstrunner)=="Slytherin"):
            s=s+event.firstrunnerscore
        elif(str(event.firstrunner)=="Gryffindor"):
            g=g+event.firstrunnerscore
        elif(str(event.firstrunner)=="Ravenclaw"):
            r=r+event.firstrunnerscore
        if(str(event.secondrunner)=="Hufflepuff"):
            h=h+event.secondrunnerscore
        elif(str(event.secondrunner)=="Slytherin"):
            s=s+event.secondrunnerscore
        elif(str(event.secondrunner)=="Gryffindor"):
            g=g+event.secondrunnerscore
        elif(str(event.secondrunner)=="Ravenclaw"):
            r=r+event.secondrunnerscore
        if(str(event.thirdrunner)=="Hufflepuff"):
            h=h+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Slytherin"):
            s=s+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Gryffindor"):
            g=g+event.thirdrunnerscore
        elif(str(event.thirdrunner)=="Ravenclaw"):
            r=r+event.thirdrunnerscore
    context = {
        'h' : h,
        's' : s,
        'g' : g,
        'r' : r,
        'events': Event.objects.filter(status='C')
    }
    return render(request, "scores.html", context)

def sponsorus(request):
    return render(request, "sponsorus.html")

def feedback(request):
    return render(request, "feedback1.html")