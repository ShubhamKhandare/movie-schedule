from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

TITLE = "Movie Schedule"
DESCRIPTION = """
We need to create a small application where everyone can view the movies on the schedule, separated by date. These movies should be in a list with the following information:

Title
Poster
Genre(s)
Rating
Year Release
Metacritic Rating
Runtime
There should be one filter and one search. The filter should be by Genre. It should be a dropdown list, populated with all genres of movies currently in our list and it should hide all movies that do not match the selected genre when clicked. Bonus points if it allows for multiple selections.

The search should be by Title. It's should be a text input that, with each character, shows each movie that matches the current string and hides each movie that doesn't.
"""
VERSION = "1.0.0"


urlpatterns = [
    path(
        "schema/",
        get_schema_view(title=TITLE, description=DESCRIPTION, version=VERSION),
        name="openapi-schema",
    ),
    path(
        "swagger-ui/",
        TemplateView.as_view(
            template_name="openapi/swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
]
