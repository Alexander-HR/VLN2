from django.shortcuts import render
from django.core.paginator import Paginator
from CastleApartments.models import Property

# Create your views here.
def home(request):
    return render(request, "index.html")

def buyer_profile(request):
    return render(request, 'buyerProfile.html')

def property_catalog(request):
    page = int(request.GET.get('page', 1))
    page_size = 16 if page == 1 else 24

    properties = Property.objects.all()
    paginator = Paginator(properties, page_size)
    page_obj = paginator.get_page(page)

    return render(request, 'index.html', {
        'properties': page_obj.object_list,
        'has_next': page_obj.has_next(),
        'next_page': page + 1
    })

def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'property_detail.html', {'property': property})
