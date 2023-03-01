from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_home, name='crud_home'),
    path('create', views.create, name='create'),
]
