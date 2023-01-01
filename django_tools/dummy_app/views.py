from django.shortcuts import render
from .models import Anime
from django.core.paginator import Paginator
# Create your views here.

def anime_list(request):
  anime_objects = Anime.objects.all()

  # Search and filter

  anime_name = request.GET.get('anime_name')

  if anime_name != '' and anime_name is not None:
    anime_objects = anime_objects.filter(name__icontains=anime_name)

  # Paginator instance
  paginator = Paginator(anime_objects,3)

  # Get current page number
  page = request.GET.get('page')

  # Items. Fetch items on current page
  anime_objects = paginator.get_page(page)

  return render(request,'dummy_app/anime_list.html',{'anime_objects':anime_objects})
