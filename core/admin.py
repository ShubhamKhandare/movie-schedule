from django.contrib import admin

from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    model = Genre


class MovieAdmin(admin.ModelAdmin):
    model = Movie


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
