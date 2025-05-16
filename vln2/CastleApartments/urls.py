from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from properties.models import Property
from django.contrib.auth import views as auth_views
from users import views as user_views



urlpatterns = [
    path('', views.property_catalog, name='home'),
    path('#/', views.buyer_profile, name='buyer_profile'),
    path('property/', views.property_detail, name='property_details'),
    path('profile/', views.seller_profile, name='seller_profile'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', user_views.signup, name='signup'),
    path('offer/', include('offers.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)