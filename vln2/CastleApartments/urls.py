from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_catalog, name='home'),
    path('profile/', views.buyer_profile, name='buyer_profile'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),

]