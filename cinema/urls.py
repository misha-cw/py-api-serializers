from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    GenreViewSet,
)

namespace = "cinema"

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
