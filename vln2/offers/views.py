from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from properties.models import Property
from offers.models import PurchaseOffer
from sellers.models import Seller
from .forms import PurchaseOfferForm
# Create your views here.

@login_required
def submitOffer(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    # Block sellers from submitting offers
    if hasattr(request.user, 'seller'):
        return HttpResponseForbidden("Sellers cannot make purchase offers.")

    if request.method == 'POST':
        form = PurchaseOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.property = property_obj
            offer.buyer = request.user
            offer.status = 'pending'
            offer.save()
            messages.success(request, "✅ Offer submitted successfully!")
            return redirect('property_detail', property_id=property_id)
    else:
        form = PurchaseOfferForm()

    return render(request, 'submitOffer.html', {
        'form': form,
        'property': property_obj
    })
