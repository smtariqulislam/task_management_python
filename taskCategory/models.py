from django.db import models
from taskModel.models import TaskModel

# Create your models here.

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    taskModel = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.name

