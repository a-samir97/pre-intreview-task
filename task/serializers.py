from rest_framework import serializers
from .models import Task, Tile

class TileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tile
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    tile = TileSerializer()
    class Meta:
        model = Task
        fields = '__all__'

