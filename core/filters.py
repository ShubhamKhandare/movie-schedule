import django_filters

from core.models import Movie


class MovieGenreFilter(django_filters.FilterSet):
    genres = django_filters.Filter(field_name="genres", lookup_expr='in')

    class Meta:
        model = Movie
        fields = "__all__"
