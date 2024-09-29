from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def get_privet(request):
    return HttpResponse('Привет!')
