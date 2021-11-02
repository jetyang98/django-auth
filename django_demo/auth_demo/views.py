from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=user, password=pwd)

        if user:
            auth.login(request, user)
            return redirect(request.GET.get("next"))

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')


@login_required
def index(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')

    return render(request, 'index.html', {"username": request.user.username})
