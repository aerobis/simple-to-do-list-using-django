from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form':form})

