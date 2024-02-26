from django.db import models


class Movie(models.Model):
    """
    A model to store information about movies on the schedule.
    """

    title = models.CharField(
        max_length=255,
        help_text="The title of the movie.",
    )
    poster = models.URLField(
        max_length=255,
        help_text="URL to the movie's poster.",
    )
    genres = models.ManyToManyField(
        "core.Genre",
        related_name="movies",
        blank=True,
        help_text="Genres of the movie.",
    )
    year_release = models.IntegerField(
        help_text="The year the movie was released.",
    )
    metacritic_rating = models.IntegerField(
        help_text="Metacritic rating of the movie.",
    )
    runtime = models.IntegerField(
        help_text="The duration of the movie in minutes.",
    )
    schedule_date = models.DateField()


class Genre(models.Model):
    """
    A model to represent different genres of movies.
    """

    name = models.CharField(
        max_length=50,
        help_text="The name of the genre.",
    )
