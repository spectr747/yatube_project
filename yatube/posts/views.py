from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, template, context)