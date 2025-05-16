from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from properties.models import Property
from django.http import JsonResponse
from django.template.loader import render_to_string
from users.models import CustomUser
from sellers.models import Seller
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "index.html")

def buyer_profile(request, user_id):
    buyer = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        data = request.POST
        updated = False

        if data.get('first_name'):
            buyer.first_name = data['first_name']
            updated = True
        if data.get('last_name'):
            buyer.last_name = data['last_name']
            updated = True
        if data.get('bio'):
            buyer.profile.bio = data['bio']
            updated = True

        if updated:
            buyer.save()
            messages.success(request, "Your profile was updated successfully.")
        else:
            messages.warning(request, "No changes detected. Please fill in at least one field.")

        return redirect('buyer_profile', user_id=buyer.id)

    return render(request, 'buyerProfile.html', {'buyer': buyer})

def guest_profile(request, user_id):
    profile = get_object_or_404(Seller, id=user_id)
    return render(request, 'guestProfile.html', {'profile': profile})

def seller_profile(request):  #, pk):
    page = int(request.GET.get('page', 1))
    page_size = 16 if page == 1 else 24

    properties = Property.objects.all()  # Later: filter by seller
    paginator = Paginator(properties, page_size)
    page_obj = paginator.get_page(page)

    return render(request, 'sellerProfile.html', {
        'properties': page_obj.object_list,
        'has_next': page_obj.has_next(),
        'next_page': page + 1
    })

def property_catalog(request):
    page = int(request.GET.get('page', 1))
    page_size = 16 if page == 1 else 24

    properties = Property.objects.all()
    paginator = Paginator(properties, page_size)
    page_obj = paginator.get_page(page)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('partials/property_cards.html', {'properties': page_obj.object_list})
        return JsonResponse({
            'html': html,
            'has_next': page_obj.has_next(),
            'next_page': page + 1
        })

    return render(request, 'index.html', {
        'properties': page_obj.object_list,
        'has_next': page_obj.has_next(),
        'next_page': page + 1
    })

def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'propertyDetails.html', {'property': property})