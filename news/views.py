from django.http import HttpResponse
from django.shortcuts import render
from .models import Teams

def team_list(request):
    
    teams= Teams.objects.all()
    return render(request, 'news/team_list.html', {'teams':teams})