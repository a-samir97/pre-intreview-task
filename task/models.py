from django.db import models

class Tile(models.Model):
    STATUS = (
        ("L", "Live"),
        ("P", "Pending"),
        ("A", "Archived")
    )

    launch_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS)

class Task(models.Model):
    TYPES = (
        ("SV", "Survey"),
        ("DC", "Discussion"),
        ("DI", "Diary")
    )

    title = models.CharField(max_length=30)
    order = models.CharField(max_length=30)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=TYPES)
    tile = models.ForeignKey(Tile, on_delete=models.CASCADE, related_name='tasks')