from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Создание продуктов")

        products_names = [
            "Холодильник",
            "Плита",
            "Тостер",
        ]

        for product_name in products_names:

            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f"Создан продукт {product.name}")

        self.stdout.write(self.style.SUCCESS("Продукт создан"))