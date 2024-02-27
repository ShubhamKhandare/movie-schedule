from rest_framework import serializers

from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def update(self, instance, validated_data):
        prev_vote_count = instance.vote_count
        instance = super().update(instance, validated_data)
        instance.vote_count = prev_vote_count + 1
        instance.save()
        return instance
