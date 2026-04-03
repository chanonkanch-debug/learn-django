from . models import Movie
from django.contrib import admin

# note: execute on server startup
admin.site.register(Movie) # adding model to admin site 