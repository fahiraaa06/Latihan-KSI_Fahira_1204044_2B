from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Post
from.models import PostModel
from .forms import PostForm
# Create your views here.

def index(request):
    posts = PostModel.objects.all()
    db = Post.objects.all()
    context ={
        'page_title':'List Apk',
        'posts' : posts,
        'title' :'Apk',
        'heading' : 'Apk',
        'subheading' : 'Postingan',
        'post' : db,
    }
    return render(request, 'apk/index.html',context)

def create(request):
    post_form = PostForm()

    if request.method == 'POST':
        PostModel.objects.create(
            judul = request.POST['title'],
            body = request.POST['body'],
            category = request.POST['category'],
        )

        return HttpResponseRedirect("/apk/")

    context = {
        'page_title' : 'Create Post',
        'post_form' :post_form
    }

    return render(request, 'apk/create.html', context)
def recent(request):
    return HttpResponse("Recent")

