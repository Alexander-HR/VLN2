from CastleApartments.models import Property
import random

# Dummy property data
addresses = ["Ocean Drive", "Mountain View", "Suburb Lane", "Forest Road", "Lakeside Ave"]

for _ in range(10):
    Property.objects.create(
        address=f"{random.randint(100, 999)} {random.choice(addresses)}",
        thumbnail="property_thumbnails/sample.jpg",  # You can update to valid path
        listing_price=random.randint(300_000, 1_200_000),
        num_rooms=random.randint(2, 7),
        square_meters=round(random.uniform(70, 250), 1),
        is_sold=random.choice([False, False, False, True])  # 75% unsold
    )

print("✅ 10 dummy properties created.")
