from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Создать заказ")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_adress="ul Pushkina, d Kolotushkina",
            promocode="SALE123",
            user=user,
        )
        self.stdout.write(f"Создан заказ {order}")