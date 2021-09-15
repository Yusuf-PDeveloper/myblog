from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostList.as_view(), name='post_detail')
]