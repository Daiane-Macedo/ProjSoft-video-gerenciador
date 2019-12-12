from django.urls import path
from . import views

urlpatterns = [
    path('users/new', views.new_user, name='new_user'),
    path('users/create', views.create_user, name='create_user')
]