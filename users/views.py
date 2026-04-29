from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from .models import Profile


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {
                'error': 'Пользователь уже существует'
            })

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )

        # добавляем телефон
        user.profile.phone = phone
        user.profile.save()

        login(request, user)
        return redirect('home')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'users/login.html', {
                'error': 'Неверный логин или пароль'
            })

        login(request, user)
        return redirect('home')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')