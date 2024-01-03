from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserProfileView.as_view(), name='users'),
    path('user/', views.UserView.as_view(), name='user'),
    path('userone/', views.UserOneView.as_view(), name='userone'),
]