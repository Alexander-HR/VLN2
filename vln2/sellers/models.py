from django.db import models

# Create your models here.
class Seller(models.Model):
    SELLER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('agency', 'Real Estate Agency'),
    ]

    user = models.OneToOneField('users.CustomUser', on_delete=models.CASCADE)
    seller_type = models.CharField(max_length=20, choices=SELLER_TYPE_CHOICES)
    
    # Only for agencies
    street_name = models.CharField(max_length=100, blank=True, null=True) 
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)

    logo = models.ImageField(upload_to='sellers/logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='sellers/cover_images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.seller_type})"
