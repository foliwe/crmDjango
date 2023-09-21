import os
import django
from faker import Faker
# Replace 'myapp' with the actual name of your Django app
from project.models import Record

# Initialize Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
django.setup()

# Create an instance of Faker
fake = Faker()

# Define the number of records you want to create
num_records = 100  # Change this to the desired number

# Generate and save random data to the Record model
for _ in range(num_records):
    record = Record(
        city=fake.city(),
        address=fake.street_address(),
        county=fake.county(),
        email=fake.email(),
        first_name=fake.first_name()
    )
    record.save()

print(f"Generated {num_records} random records.")
