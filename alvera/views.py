from django.shortcuts import render
# ----------------------------------------------
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
# from .forms import CreateNewTask, CreateNewProject
# ----------------------------------------------


# Create your views here.
def home(request):
    return render(request, 'home.html')