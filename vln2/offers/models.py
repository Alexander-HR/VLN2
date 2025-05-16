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
    
class FinalizedOffer(models.Model):
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('mortgage', 'Mortgage'),
    ]

    purchase_offer = models.OneToOneField(PurchaseOffer, on_delete=models.CASCADE, related_name='finalized_offer')
    # Contact information
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    national_id = models.CharField(max_length=10)
    
    # Payment information
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

    # Credit card information
    cardholder_name = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiry_date = models.CharField(max_length=5, blank=True, null=True)  # Format: MM/YY
    cvc = models.CharField(max_length=3, blank=True, null=True)

    # Bank transfer information
    bank_account_number = models.CharField(max_length=20, blank=True, null=True)

    # Mortgage information
    mortgage_provider = models.CharField(max_length=100, blank=True, null=True)

    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Finalized offer for {self.purchase_offer.property.address}"