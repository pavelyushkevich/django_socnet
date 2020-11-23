from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.post, name='post'),
    path('<int:post_id>/add_comment', views.add_comment, name='add_comment'),
    path('add_post', views.add_post, name='add_post'),
]
