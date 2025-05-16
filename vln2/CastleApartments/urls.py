from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from properties.models import Property


urlpatterns = [
    path('', views.property_catalog, name='home'),
    path('#/', views.buyer_profile, name='buyer_profile'),
    path('property/', views.property_detail, name='property_details'),
    path('profile/', views.seller_profile, name='seller_profile'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)