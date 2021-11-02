from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'accounts/login/', views.login, name='login'),
    path(r'accounts/logout/', views.logout, name='logout'),
]