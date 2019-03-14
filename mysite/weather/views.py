from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the weather app INDEX.")
def weather(request):
    return HttpResponse("Hello, welcome to the weather app.")