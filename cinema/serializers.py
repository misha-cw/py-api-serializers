from rest_framework import serializers
from cinema.models import (
    Genre,
    Actor,
    Movie,
    MovieSession,
    CinemaHall,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)
