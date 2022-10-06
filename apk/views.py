from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def recent(request):
    return HttpResponse("RECENT")
# Create your views here.
