from rest_framework import serializers
from .models import Task, Tile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TileSerializer(serializers.ModelSerializer):
    related_tasks = serializers.SerializerMethodField()

    class Meta:
        model = Tile
        fields = '__all__'
    
    def get_related_tasks(self, obj):
        related_task = obj.tasks.all()
        related_task_serialized = TaskSerializer(related_task, many=True)
        return related_task_serialized.data