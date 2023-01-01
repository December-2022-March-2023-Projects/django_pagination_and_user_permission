from django.shortcuts import render
from .models import Anime
from django.core.paginator import Paginator
# Create your views here.

def anime_list(request):
  anime_objects = Anime.objects.all()

  # Paginator instance
  paginator = Paginator(anime_objects,3)

  # Get current page number
  page = request.GET.get('page')

  # Items. Fetch items on current page
  anime_objects = paginator.get_page(page)

  return render(request,'dummy_app/anime_list.html',{'anime_objects':anime_objects})
