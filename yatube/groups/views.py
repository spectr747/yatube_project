from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)