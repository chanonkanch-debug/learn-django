from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from . models import Movie


def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html',  {'movies': data}) 

def home(request):
    return HttpResponse("Home Page")

#get
def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

#post
def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save() 
        return HttpResponseRedirect('/movies')
    
    return render(request, 'movies/add.html')

#delete
def delete(request, id):
    try:  
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    movie.delete()
    
    return HttpResponseRedirect('/movies')