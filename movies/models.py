from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.TextField(default="")
    
    def __str__(self):
        return f'{self.name}'
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)
    description = models.TextField(default="")
    rating = models.FloatField(default=0.0)
    poster_url = models.URLField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return f'{self.title} from {self.year}'