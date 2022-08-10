from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'mainsite/index.html', locals())

def about(request):
    return render(request, 'mainsite/about.html')

def ministry(request):
    return render(request, 'mainsite/ministry.html')

def sermons(request):
    return render(request, 'mainsite/sermons.html')

def events(request):
    return render(request, 'mainsite/events.html')

def blog(request):
    return render(request, 'mainsite/blog.html')

def blog_single(request):
    return render(request, 'mainsite/blog-single.html')

def contact(request):
    return render(request, 'mainsite/contact.html')
