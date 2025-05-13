from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_catalog, name='home'),
    path('#/', views.buyer_profile, name='buyer_profile'),
    path('property/', views.property_detail, name='property_details'),
    path('profile/', views.seller_profile, name='seller_profile'),


]