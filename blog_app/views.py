from django.shortcuts import render
from django.views.generic import ListView

from .forms import CommentForm
from .models import Blog, Category, Comment

class Home(ListView):
    model = Blog
    template_name = "blog.html"


def detail(request, pk):
    post = Blog.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context={
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, "blog-detail.html", context)


def category(request, category):
    posts = Category.objects.filter(categories_name_contain=category).order_by('-created_on')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, "category.html", context)