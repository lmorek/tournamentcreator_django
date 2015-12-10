from django.db import models
from django.utils import timezone

# Create your models here.
class Teams(models.Model):
    author = models.ForeignKey('auth.User')
    teamName = models.CharField(max_length=200)
    capitan = models.CharField(max_length=200)
    firstPlayer = models.CharField(max_length=200)
    secondPlayer = models.CharField(max_length=200)
    thirdPlayer = models.CharField(max_length=200)
    fourthplayer = models.CharField(max_length=200)
    fifthPlayer = models.CharField(max_length=200)
    sixthplayer = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.teamName