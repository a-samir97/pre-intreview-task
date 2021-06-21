from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskModelViewSet, TileModelViewSet

router = DefaultRouter()
router.register("tasks", TaskModelViewSet)
router.register("tiles", TileModelViewSet)

urlpatterns = [
    path("", include(router.urls))
]