from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render
from . models import Movie, Genre, Review

from django.http import JsonResponse
from . serializer import MovieSerializer

# ───── Movie Views ─────

def home(request):
    return HttpResponse("Home Page")

def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html',  {'movies': data}) 

#get
def detail(request, id):
    data = Movie.objects.get(pk=id)
    reviews = Review.objects.filter(movie=data)
    return render(request, 'movies/detail.html', {'movie': data, 'reviews': reviews})

#post
def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    genre_ids = request.POST.getlist('genre')
    description = request.POST.get('description')
    rating = request.POST.get('rating')
    
    if title and year and genre_ids:
        movie = Movie(
            title=title, 
            year=year,
            description=description,
            rating=rating)
        movie.save() 
        movie.genre.set(genre_ids)
        return HttpResponseRedirect('/movies')
    
    genre = Genre.objects.all()
    return render(request, 'movies/add.html', {'genres': genre})

#update
def edit(request, id):
    movie = Movie.objects.get(pk=id)

    if request.method == 'POST':
        movie.title = request.POST.get('title')
        movie.year = request.POST.get('year')
        movie.description = request.POST.get('description')
        movie.rating = request.POST.get('rating')
        genre_ids = request.POST.getlist('genre')
        
        movie.save()
        movie.genre.set(genre_ids)
        return HttpResponseRedirect('/movies')
    
    genres = Genre.objects.all()
    return render(request, 'movies/add.html', {'movie': movie, 'genres': genres})

#delete
def delete(request, id):
    try:  
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')

    movie.delete()
    
    return HttpResponseRedirect('/movies')

# ───── Review Views ─────

#post
def add_review(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    
    if request.method == 'POST':
        reviewer_name = request.POST.get('reviewer_name')
        comment = request.POST.get('comment')
        score = request.POST.get('score')
        
        if reviewer_name and comment and score:
            review = Review(
                movie=movie,
                reviewer_name=reviewer_name,
                comment=comment,
                score=score
            ) 
            review.save()
            return HttpResponseRedirect(f'/movies/{movie_id}')    

    return render(request, 'movies/add_review.html', {'movie': movie})

# delete review
def delete_review(request, movie_id, review_id):
    try:    
        review = Review.objects.get(pk=review_id, movie_id=movie_id)
    except Review.DoesNotExist:
        raise Http404('Movie does not exist')
    
    review.delete()
    
    return HttpResponseRedirect(f'/movies/{movie_id}')
    