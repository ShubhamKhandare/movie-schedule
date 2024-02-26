from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Genre, Movie

User = get_user_model()


class MovieFactory(DjangoModelFactory):
    class Meta:
        model = Movie

    title = factory.Faker("bs")
    poster = factory.Faker("url")
    year_release = factory.Faker("random_int")
    metacritic_rating = factory.Faker("random_int")
    runtime = factory.Faker("random_int")

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        if not create:
            return
        # if related model instances are provided, add them to the relation
        if extracted:
            for model in extracted:
                self.genres.add(model)
        # by default the relation is empty


class GenreFactory(DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker("bs")
