from django.urls import path
from . import views

app= 'index'

urlpatterns = [
    path('', views.index, name='index'),
    
]
