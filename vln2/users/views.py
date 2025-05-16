from django.shortcuts import render, redirect
from users.forms import CustomUserSignupForm
from sellers.models import Seller
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user_type = form.cleaned_data.get('user_type')

            if user_type == 'seller':
                Seller.objects.create(user=user)


            messages.success(request, "✅ You have successfully created your account!")

            return redirect('login')  # or wherever you want to go next
    else:
        form = CustomUserSignupForm()

    return render(request, 'signup.html', {'form': form})
