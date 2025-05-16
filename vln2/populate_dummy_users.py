from users.models import CustomUser
from faker import Faker

fake = Faker()

for i in range(10):
    username = f"user_{i}_{fake.user_name()}"
    email = fake.email()

    if not CustomUser.objects.filter(username=username).exists():
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password='test1234'
        )
        print(f"✅ Created: {username}")
    else:
        print(f"⚠️ Skipped (already exists): {username}")

print("✅ 10 dummy CustomUser accounts created (or skipped if duplicates existed).")
