from django.urls import path
from . import views

urlpatterns = [
    path('users/new', views.new_user, name='new_user')
]