from django.shortcuts import render
from django.http import HttpResponse

def test_view(requests):
    return HttpResponse("Hello World")
# Create your views here.
