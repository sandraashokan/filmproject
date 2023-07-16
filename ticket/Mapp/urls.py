"""
URL configuration for ticket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Mapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'Mapp'
urlpatterns = [
    path('',views.home,name="home"),
    path('add1',views.add1,name="add1"),
    path('delete/<int:p>', views.delete_film, name="delete"),
    path('edit/<int:p>', views.edit_film, name="edit"),



]
