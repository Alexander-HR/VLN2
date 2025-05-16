from sellers.models import Seller
from users.models import CustomUser
from faker import Faker
from random import choice

fake = Faker()

users = CustomUser.objects.all()[:10]

if not users:
    print("❌ No users found to link with sellers. Please create CustomUser entries first.")
else:
    for user in users:
        seller_type = choice(['individual', 'agency'])

        Seller.objects.create(
            user=user,
            seller_type=seller_type,
            street_name=fake.street_name() if seller_type == 'agency' else "",
            city=fake.city() if seller_type == 'agency' else "",
            postal_code=fake.postcode() if seller_type == 'agency' else "",
            logo='sellers/logos/sample_logo.jpg',
            cover_image='sellers/cover_images/sample_cover.jpg',
            bio=fake.paragraph(nb_sentences=3)
        )

    print("✅ 10 dummy sellers created and linked to existing users.")
