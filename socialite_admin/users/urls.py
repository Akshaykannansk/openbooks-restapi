from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegistrationView.as_view(), name='register'),
    path('user-list', userlist.as_view(), name='userlist'),
    path('userlist', userListview.as_view(), name= 'user_list'),
    path('user-detail/<int:pk>/', userdetail.as_view(),name= 'userdetail'),

]
