from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import*
from django.urls import reverse
from django.views.generic import ListView, DetailView


def Home(request):
    context = {
        'image': AddProfileImage.objects.all(),
        'posts': Project.objects.all().order_by('-id')
    }
    return render(request, 'index.html', context)



class Portfolio(ListView):
    model = Project
    paginate_by = 6
    order_by = 'date'
    template_name = "portfolio.html"



class Detail(DetailView):
    model = Project
    template_name = "detail.html"



def category(request, name):
    q = Category.objects.get(name__icontains=name)
    posts = Project.objects.filter(categories__name__contains=name)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts, 'query': q,
        'page_obj': page_obj,
    }
    return render(request, "category.html", context)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        msg = Contact(name=name, email=email, number=number, body=message)
        msg.save()
        messages.success(request, 'Message sent')
        return redirect(reverse('/'))
    else:
        messages.error(request, 'Error contacting Optimize, please recheck the form')
        return redirect(reverse('/'))
