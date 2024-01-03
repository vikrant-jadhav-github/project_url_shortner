from django.urls import path
from . import views

urlpatterns = [
    path('', views.UrlShortnerView.as_view()),
    path('<str:pk>/', views.UrlShortnerView.as_view()),
]