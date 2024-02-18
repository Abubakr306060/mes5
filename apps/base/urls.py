from django.urls import path
from apps.base.views import *
urlpatterns = [
    path('', index , name='index'),
    path('blog/<int:id>//', blog , name='blog'),
    path('blog/<int:id>//', comments , name='blog'),
     path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]