from django.shortcuts import render,get_object_or_404
from .models import Article,Catergory

# Create your views here.
def home(request):
    context={
        "articles":Article.objects.published(),
        "category":Catergory.objects.filter(status=True)
    }
    return render(request,"blog/home.html",context)

def detail(request,slug):
    context={
        "article":get_object_or_404(Article.objects.published(),slug=slug)
    }
    return render(request,"blog/detail.html",context)
 

def category(request,slug):
    context={
        "category":get_object_or_404(Catergory,slug=slug,status=True)
    }
    return render(request,"blog/category.html",context)
