from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title=models.CharField(max_length=100)
    decription=models.TextField()
    assignDate=models.DateField()
    is_completed =models.BooleanField(default=False)
