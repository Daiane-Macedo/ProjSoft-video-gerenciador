from django.shortcuts import render

def new_user(request):
    return render(request, 'users/new_user.html', {})