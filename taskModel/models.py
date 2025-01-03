from django.db import models

# Create your models here.

from  taskCategory.models import TaskCategory


class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    decription=models.TextField()
    assignDate=models.DateField()
    category = models.ManyToManyField(TaskCategory)
    is_completed =models.BooleanField(default=False)

    def __str__(self):
        return self.title
