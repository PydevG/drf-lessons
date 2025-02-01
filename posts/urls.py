from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('posts/', views.PostListCreateView.as_view(), name='posts'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='singlepost'),

]