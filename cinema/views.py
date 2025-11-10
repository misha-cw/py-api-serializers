from rest_framework import viewsets
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieRetrieveSerializer,
    MovieSessionSerializer,
    MovieSesionRetrieveSerializer,
    MovieSessionListSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve",):
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset.all()


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action == "retrieve":
            return MovieSesionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve",):
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset.all()
