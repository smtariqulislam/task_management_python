from django.shortcuts import render, redirect
from taskModel.models import TaskModel

def home(request):
    data = TaskModel.objects.all()
    return render(request, 'home.html' , {'data':data}) 