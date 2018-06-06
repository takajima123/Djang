from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostUpdateDelete.as_view()),
    path('create/', views.PostCreateSerializer.as_view()),
]

