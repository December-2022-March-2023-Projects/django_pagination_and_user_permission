from django.shortcuts import render
from .models import Anime
# Create your views here.

def anime_list(request):
  anime_objects = Anime.objects.all()
  return render(request,'dummy_app/anime_list.html',{'anime_objects':anime_objects})
  