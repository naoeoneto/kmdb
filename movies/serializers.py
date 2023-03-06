from rest_framework import serializers
from .models import Movie
from genres.serializers import GenreSerializer
from genres.models import Genre

class MovieSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        my_genres = validated_data.pop('genres')
        my_movie = Movie.objects.create(**validated_data)
        
        for genre in my_genres:
            new_genre = Genre.objects.filter(name__iexact=genre['name']).first()
            
            if not new_genre:
                new_genre = Genre.objects.create(**genre)
            my_movie.genres.add(new_genre)

        return my_movie

    
    class Meta:
        model = Movie
        fields = ["id", "title", "duration", "premiere", "budget", "overview", "genres"]
        read_only_fields = ["id"]
        