from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):

    db = Post.objects.all()
    context = {
        'title' : 'Apk',
        'heading' : 'Apk',
        'subheading' : 'postingan',
        'post' : db,
    }
    return render(request, 'apk/index.html', context)

def recent(request):
    return HttpResponse("Recent")

