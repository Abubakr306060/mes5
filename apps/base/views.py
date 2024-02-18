from django.shortcuts import render, redirect
from apps.base.models import *
from django.contrib.auth.models import User
# from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Создание пользователя
        user = User.objects.create_user(username=username, email=email, password=password)
        # Дополнительные действия, например, вход пользователя
        return redirect('login')
    else:
        return render(request, 'registration/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Аутентификация пользователя
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Дополнительные действия, например, перенаправление на профиль
            return redirect('profile')
        else:
            # Обработка ошибки аутентификации
            return render(request, 'registration/signin.html', {'error': 'Invalid login credentials!'})
    else:
        return render(request, 'registration/signin.html')

# Create your views here.

def index(request):
    settings = Settings.objects.latest('id')
    blog = News.objects.all()
    return render(request, "demo25.html", locals())

def blog(request, id):
    blog = News.objects.get(id=id)
    return render(request, "blog-post.html", locals())

def comments(request):
    comments = Comments.objects.all()  # Получение всех комментариев из базы данных
    context = {'comments': comments}
    return render(request, 'blog-post.html', context, locals())


# def add_comment(request):
#     if request.method == 'POST':
#         author = request.POST.get('author')
#         email = request.POST.get('email')
#         body = request.POST.get('body')
#         avatar = request.FILES.get('avatar')  # Получаем файл изображения из запроса
#         comment = Comments(author=author, email=email, body=body, avatar=avatar)
#         comment.save()
#         return redirect('blog/<int:id>//')  # Перенаправляем на страницу успешной отправки комментария
#     return render(request, 'blog-post.html')


