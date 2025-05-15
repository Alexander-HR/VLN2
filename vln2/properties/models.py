from django.db import models

# Create your models here.
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('villa', 'Villa'),
        ('house', 'House'),
        ('townhouse', 'Townhouse'),
        ('apartment', 'Apartment'),
    ]

    seller = models.ForeignKey('sellers.Seller', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)

    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_date = models.DateField(auto_now_add=True)
    sold = models.BooleanField(default=False)
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)  # in square meters

    # Might need to fix the upload_to path
    thumbnail = models.ImageField(upload_to='property_thumbnails/', blank=True, null=True)
    images = models.ImageField(upload_to='properties/images/', blank=True, null=True)


    def __str__(self):
        return f"{self.property_type} in {self.city} - {self.price} ISK"
    
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='image_gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='properties/images/')
    
    def __str__(self):
        return f"Image for {self.property.address}"