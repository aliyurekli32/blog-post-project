from .models import Category, Blog
from faker import Faker
from datetime import datetime

def run():
    fake = Faker(['en-US'])
    categories = (
        "Politics",
        "Sports",
        "Millitary",
        "Travel",
        "Showbiz"
    )

    for category in categories:
        new_category = Category.objects.create(name = category)
        for _ in range(30):
            Blog.objects.create(category = new_category, title = fake.company(), content = fake.text())
    
    print('Finished')