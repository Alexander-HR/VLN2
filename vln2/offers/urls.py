from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:property_id>/', views.submitOffer, name='submit_offer'),
]
