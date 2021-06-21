from rest_framework.viewsets import ModelViewSet
from .models import Task, Tile
from .serializers import TaskSerializer, TileSerializer


class TaskModelViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TileModelViewSet(ModelViewSet):
    queryset = Tile.objects.all()
    serializer_class = TileSerializer