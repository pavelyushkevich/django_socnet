from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    # path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
]
