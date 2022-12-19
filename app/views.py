from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
# def Menu(request):
#     return render(request, 'index.html')

# def Nosotros(request):
#     return render(request, 'nosotros.html')

# def Info(request):
#     return render(request, 'informacion.html')

# def Prueba(request):
#     return render(request, 'prueba.html')

# def index(request):
#     return render(request, 'index.html')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

# Header


class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class About(ListView):
    model = Post
    template_name = 'nosotros.html'


class News(ListView):
    model = Post
    template_name = 'anuncios.html'


class Contact(ListView):
    model = Post
    template_name = 'contacto.html'


class LoginView(ListView):
    model = Post
    template_name = 'login.html'


class Commentary(CreateView):
    model = Post
    template_name = 'post.html'
    fields = '__all__'
