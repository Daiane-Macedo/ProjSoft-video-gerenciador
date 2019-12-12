from django.shortcuts import render, redirect
from .forms import UserForm

def new_user(request):
    form = UserForm()
    return render(request, 'users/new_user.html', { 'form': form })

def create_user(request):
    form = UserForm(request.POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.create()
        return redirect('home')
    else:
        return redirect('new_user')