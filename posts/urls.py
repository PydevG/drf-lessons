from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('posts/', views.list_posts, name='posts'),
    path('<int:post_id>/', views.single_post, name='singlepost')

]