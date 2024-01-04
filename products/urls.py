from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('search/', views.ProductOneView.as_view()),
    path('description/', views.ProductDescriptionView.as_view()),
    path('description/search/', views.ProductDescriptionOneView.as_view()),
    path('product_description/', views.ProductDescriptionView.as_view()),
    path('product_description/search/', views.ProductDescriptionOneView.as_view()),
    path('user/', views.ProductUserView.as_view()),
    path('user/search/', views.ProductUserOneView.as_view()),

]