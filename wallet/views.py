from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

@api_view()
def welcome(request):
    return HttpResponse("Welcome to Welcome Page")

def greeting(request, name):
    return render(request, 'hello.html', {'name': name})
