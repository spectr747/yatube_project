from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def group_posts(request, slug):
    return HttpResponse(f'Название группы - {slug}')