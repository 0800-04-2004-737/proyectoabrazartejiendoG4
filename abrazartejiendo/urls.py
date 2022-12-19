"""abrazartejiendo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import HomeView, ArticleDetailView, About, News, LoginView, Contact, Commentary

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('menu/', include('app.urls')),
    # path('información/', views.Info),
    # path('prueba/', views.Prueba),
    # path('nosotros/', views.Nosotros),

    path('menu/', HomeView.as_view(), name="home"),
    path('nosotros/', About.as_view(), name="nosotros"),
    path('noticias/', News.as_view(), name="noticias"),
    path('contacto/', Contact.as_view(), name="contacto"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('login/', LoginView.as_view(), name="login"),
]
