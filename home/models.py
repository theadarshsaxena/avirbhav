from django.db import models
from datetime import datetime
from django.utils.text import slugify

class Team(models.Model):
    name = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

# Create your models here.
class Event(models.Model):
    # TEAMS = (
    #     ('R', 'Ravenclaw'),
    #     ('G', 'Gryffindor'),
    #     ('H', 'Hufflepuff'),
    #     ('S', 'Slytherin')
    # )
    STATUS = (
        ('C', 'Completed'),
        ('O', 'Ongoing'),
        ('U', 'Upcoming')
    )
    title = models.CharField(max_length=50)
    eventnum = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, unique=True, default='avirbhav-event-' + datetime.now().strftime('%Y-%m-%d-%H-%M'))
    # score = models.CharField(max_length=100)
    # winner = models.CharField(max_length=1, choices=TEAMS, blank=True)
    # firstrunner = models.CharField(max_length=1, choices=TEAMS, blank=True)
    # secondrunner = models.CharField(max_length=1, choices=TEAMS, blank=True)
    # last = models.CharField(max_length=1, choices=TEAMS, blank=True)
    winner = models.ForeignKey(Team, verbose_name =u'Winner', on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_winner')
    winnerscore = models.IntegerField("Winner Score", default=0)
    firstrunner = models.ForeignKey(Team, verbose_name =u'First Runner Up', on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_firstrunner')
    firstrunnerscore = models.IntegerField('First Runner up Score', default=0)
    secondrunner = models.ForeignKey(Team, verbose_name =u"Second Runner Up", on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_secondrunner')
    secondrunnerscore = models.IntegerField('Second Runner Up Score', default=0)
    thirdrunner = models.ForeignKey(Team, verbose_name =u'Third Runner Up', on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_thirdrunner')
    thirdrunnerscore = models.IntegerField('Third Runner Up Score', default=0)
    penalty = models.CharField(max_length=100, blank=True)
    startdate = models.DateField()
    enddate = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS, default='U')
    about = models.TextField(max_length=500)
    image = models.URLField(default="http://cdn.avirbhav.tech/avirbhav.png")

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    batch = models.CharField(max_length=4)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Scores(models.Model):
    Ravenclaw = models.IntegerField(default=0)
    Gryffindor = models.IntegerField(default=0)
    Hufflepuff = models.IntegerField(default=0)
    Slytherin = models.IntegerField(default=0)
    
    def __str__(self):
        return "Score"

