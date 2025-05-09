from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")
def buyer_profile(request):
    return render(request, 'buyerProfile.html')