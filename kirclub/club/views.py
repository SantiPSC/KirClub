from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()    
    return render(request, 'index.html', context={"recetas": posts})

def receta(request):
    return render(request, 'receta.html')