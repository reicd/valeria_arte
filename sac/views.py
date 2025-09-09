from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Definir uma view baseada em função.
def index(request):
    return HttpResponse("Hello, world. You're at the sac index.")
# Definir uma view baseada em função.
def about(request):
    return HttpResponse("This is the about page of the sac app.")
