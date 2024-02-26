from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from . import permissions
from .filters import MovieGenreFilter
from .models import Genre, Movie
from .serializers import GenreSerializer, MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.GenrePermission,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().prefetch_related().order_by("-schedule_date")
    serializer_class = MovieSerializer
    permission_classes = (permissions.MoviePermission,)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = MovieGenreFilter
    search_fields = ["title"]

