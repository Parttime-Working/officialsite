from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    msg = 'Hello'
    now = datetime.now()
    hour = now.timetuple().tm_hour
    return render(request, 'mainsite/index.html', locals())
