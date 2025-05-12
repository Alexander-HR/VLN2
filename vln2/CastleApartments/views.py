from django.shortcuts import render
from django.core.paginator import Paginator
from CastleApartments.models import Property
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request, "index.html")

def buyer_profile(request):  #, pk):
    return render(request, 'buyerProfile.html')
    """
    userProfile = userProfile.objects.get(pk=pk)
    return render(request, 'buyerProfile.html', {'user': user})
    """

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

def property_detail(request):   #, pk):
    return render(request, 'propertyDetails.html')
    """
    property = Property.objects.get(pk=pk)
    return render(request, 'property_detail.html', {'property': property})
    """