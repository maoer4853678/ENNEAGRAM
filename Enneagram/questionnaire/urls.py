from django.contrib import admin
from django.urls import path,include
from . import views
from . import apis

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('save', apis.save, name='save'),
]