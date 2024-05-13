from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name="home"),
    path('burger/', views.burger, name="burger"),
    path('AddOn/', views.AddOn, name="AddOn"),
    path('order/', views.order, name="order"),
    path('success/', views.success, name="success"),
    ]
