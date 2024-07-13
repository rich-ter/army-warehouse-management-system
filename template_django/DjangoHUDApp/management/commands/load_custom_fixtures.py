import json
from django.core.management.base import BaseCommand
from django.conf import settings
from DjangoHUDApp.models import Product, ProductCategory, ProductUsage, Group

class Command(BaseCommand):
    help = 'Load custom fixtures and create categories and usages if they do not exist'

    def handle(self, *args, **options):
        with open(settings.BASE_DIR / 'DjangoHUDApp/fixtures/products.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                category_name = item['fields']['category']
                usage_name = item['fields']['usage']

                category, created = ProductCategory.objects.get_or_create(name=category_name)
                usage, created = ProductUsage.objects.get_or_create(name=usage_name)

                owners = [Group.objects.get(pk=owner_id) for owner_id in item['fields']['owners']]

                product = Product(
                    name=item['fields']['name'],
                    batch_number=item['fields']['batch_number'],
                    unit_of_measurement=item['fields']['unit_of_measurement'],
                    image=item['fields']['image'],
                    category=category,
                    usage=usage,
                    description=item['fields']['description'],
                )
                product.save()
                product.owners.set(owners)
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded fixtures and created missing categories/usages.'))
