from django.db import models

# Create your models here.
class PurchaseOffer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    property = models.ForeignKey('properties.Property', on_delete=models.CASCADE)
    buyer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Offer for {self.property.address} by {self.buyer.username} - {self.offer_price} ISK"