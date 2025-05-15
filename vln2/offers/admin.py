from django.contrib import admin
from .models import PurchaseOffer, FinalizedOffer

# Register your models here.

admin.site.register(PurchaseOffer)
admin.site.register(FinalizedOffer)