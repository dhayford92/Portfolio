from django.shortcuts import render
from .models import*
from blog_app.models import Blog


def index(request):
    posts = Project.objects.all().order_by('-id')
    category = Category.objects.all()
    latest_post = Blog.objects.all().order_by('-id')
    context = {
        'posts': posts,
        'category': category,
        'latest_blog': latest_post
    }
    return render(request, "index.html", context)

def portfolio(request):
    posts = Project.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, "portfolio.html", context)

def detail(request, pk):
    post = Project.objects.get(pk=pk)
    return render(request, "detail.html")

def category(request, cats):
    category = Category.objects.filter(categories=cats)
    return render(request, "category.html", {'category': category})
