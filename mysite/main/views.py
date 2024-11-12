from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(respone):
    return HttpResponse("Janek")

def v1(respone):
    return HttpResponse("Cianek")