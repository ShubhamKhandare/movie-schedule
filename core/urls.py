from rest_framework import routers

from .views import GenreViewSet, MovieViewSet

core_router = routers.SimpleRouter()
core_router.register(r"core/genre", GenreViewSet)
core_router.register(r"core/movie", MovieViewSet)
