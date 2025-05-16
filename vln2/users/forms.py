from django import forms
from users.models import CustomUser

class CustomUserSignupForm(forms.ModelForm):
    USER_TYPE_CHOICES = [
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    ]

    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email', 'username',
            'password', 'profile_picture'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # 🔒 hashes the password
        if commit:
            user.save()
        return user
