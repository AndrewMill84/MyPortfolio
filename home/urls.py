from django.contrib import admin
from django.urls import path, include
from home import views
#from home import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('projects', views.projects, name='Projects' ),
    path('about', views.about, name='About' ),
    path('contact', views.contact, name='Contact' ),
]
