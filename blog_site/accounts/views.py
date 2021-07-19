from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_page(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = redirect('/articles/')
            return response
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    response = redirect('/articles/')
    return response


def register_page(request):
    form = CreateUserForm()
    if request.POST:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
                
            response = redirect('/articles/')
            return response

    context = {'form':form}
    return render(request, 'accounts/register.html',context)
