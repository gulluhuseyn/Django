from django.shortcuts import render
from .models import Article
# Create your views here.
def home_view(request):
    articles = Article.objects.all()
    return render(request, "index.html" ,{'articles':articles})
def about_view(request):
    return render(request, "about.html")
def contact_view(request):
    return render(request, "contact.html")