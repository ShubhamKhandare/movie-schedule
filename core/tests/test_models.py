from django.test import TestCase

from ..models import Genre, Movie
from .factories import GenreFactory, MovieFactory


class MovieTestCase(TestCase):
    def test_create_movie(self):
        """Test that Movie can be created using its factory."""

        obj = MovieFactory()
        assert Movie.objects.all().get() == obj


class GenreTestCase(TestCase):
    def test_create_genre(self):
        """Test that Genre can be created using its factory."""

        obj = GenreFactory()
        assert Genre.objects.all().get() == obj
