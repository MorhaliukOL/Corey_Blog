from django.shortcuts import render
from .models import Posts

def home(request):
    content = {
        'posts': Posts.objects.all()
    }
    return render(request, 'pages/home.html', content)

def about(request):
    return render(request, 'pages/about.html', {'title': 'About page'})
