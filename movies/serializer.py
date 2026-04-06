from rest_framework import serializers
from . models import Movie, Genre

# Python Object  ──► Serializer ──► JSON
# JSON           ──► Serializer ──► Python Object

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description']

class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True) # nest the genre serializer
    genre_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), source='genre', write_only=True
    )
    
    class Meta:
        model = Movie
        fields = ['title', 'year', 'genre', 'genre_ids', 'description', 'rating']
        
