from rest_framework import serializers

from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "poster",
            "genres",
            "year_release",
            "metacritic_rating",
            "runtime",
        ]
