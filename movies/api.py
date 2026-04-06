from . models import Movie, Genre
from django.http import JsonResponse
from . serializer import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

### CRUD ###

# READ & POST
@api_view(['GET', 'POST'])
def movies_list(request, format=None):
    
    if request.method == 'GET':    
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response({'movies': serializer.data})
    
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data) # get request from object
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# READ 1, UPDATE, DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id, format=None):
    
    try:
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    



