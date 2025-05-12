from django.db import models

# Create your mfrom django.db import models

class Property(models.Model):
    address = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='property_thumbnails/')
    listing_price = models.DecimalField(max_digits=12, decimal_places=2)
    num_rooms = models.IntegerField()
    square_meters = models.FloatField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.address