from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Group

# Create your views here.
def index(request):
    
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
   
    group = get_object_or_404(Group, slug=slug)
    # posts = Post.objects.filter(group=group).order_by('-pub_date')[:-10]
    posts = group.posts.all().order_by("-pub_date")
    context = {
        # 'slug': slug,
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)