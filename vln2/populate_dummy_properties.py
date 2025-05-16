from properties.models import Property, PropertyImage
from sellers.models import Seller
from random import randint, choice, uniform
from faker import Faker

fake = Faker()
seller = Seller.objects.first()

if not seller:
    print('❌ No sellers found in the database. Please add one first.')
else:
    for _ in range(10):
        property = Property.objects.create(
            seller=seller,
            address=fake.street_address(),
            city=choice(['Reykjavík', 'Kópavogur', 'Hafnarfjörður', 'Akureyri']),
            postal_code=choice(['101', '200', '220', '600']),
            description=choice([
                "A beautiful and spacious family home.",
                "Modern apartment with ocean views.",
                "Charming townhouse near the city center.",
                "Luxury villa with private garden and garage."
            ]),
            property_type=choice(['villa', 'house', 'townhouse', 'apartment']),
            listing_price=randint(30000000, 99000000),  # Max must be under 100,000,000
            rooms=randint(3, 8),
            bedrooms=randint(1, 5),
            bathrooms=randint(1, 3),
            area=round(uniform(70, 240), 2),
            sold=choice([False, False, True]),
            thumbnail='property_thumbnails/sample.jpg'
        )

        for img in ['properties/images/sample1.jpg', 'properties/images/sample2.jpg']:
            PropertyImage.objects.create(property=property, image=img)

    print("✅ 10 dummy properties created with images.")
