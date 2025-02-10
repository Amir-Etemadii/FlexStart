from django.shortcuts import render, redirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def log_in(request):

    if request.user.is_authenticated:
        return redirect('home:index')
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            raise Http404()

    return render(request, 'account/log-in.html', {})



def register(request):
    errors= []

    if request.user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print('ok 1')

        if password1 != password2:
            errors.append("Passwords must match")
            return render(request, 'account/register.html', context={'errors':errors})
        elif User.objects.filter(username=username).exists():
            errors.append("Username already taken")
            return render(request, 'account/register.html', context={'errors':errors})
        print('ok 2')

        user= User.objects.create_user(username=username, email=email, password=password1)

        login(request, user)
        print('ok 3')
        return redirect('home:index')
    return render(request, 'account/register.html', {})




def log_out(request):
    logout(request)
    return redirect('home:index')