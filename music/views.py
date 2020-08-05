from django.shortcuts import render
from django.http import HttpResponse
from .models import Music

# Create your views here.
def my_songs(request):
    mymusic = Music.objects.all()
    return render(request, 'music/my_songs.html', {'mymusic':mymusic})
