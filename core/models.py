from django.db import models


class Movie(models.Model):
    """
    A model to store information about movies on the schedule.
    """
    thumbnail = models.URLField(
        max_length=1000,
        help_text="The thumbnail of the movie"
    )
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
    vote_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id} : {self.title}"


class Genre(models.Model):
    """
    A model to represent different genres of movies.
    """

    name = models.CharField(
        max_length=50,
        help_text="The name of the genre.",
    )

    def __str__(self):
        return f"{self.id} : {self.name}"
