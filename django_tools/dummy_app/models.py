from django.db import models

# Create your models here.
class Anime(models.Model):

  def __str__(self):
    return self.name

  name = models.CharField(max_length=200)
  episodes = models.IntegerField(default=12)
  genre = models.CharField(max_length=20, default='Action')
  rating = models.FloatField()
