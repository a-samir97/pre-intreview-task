from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TileViewSet

router = DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("tiles", TileViewSet)

urlpatterns = [
    path("", include(router.urls))
]
