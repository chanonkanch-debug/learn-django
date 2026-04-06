from . models import Movie
from . models import Genre
from django.contrib import admin

# note: execute on server startup
admin.site.register(Movie) # adding model to admin site
admin.site.register(Genre) 