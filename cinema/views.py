from rest_framework import viewsets
from cinema.models import (
    Genre,
    Actor,
    Movie,
    MovieSession,
    CinemaHall,
)
from cinema.serializers import (
    GenreSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
