from django.test import TestCase
from .models import MenuItem


class MenuItemTestCase(TestCase):
    def test_get_item(self):
        print('22222')
        item = MenuItem.objects.create(Title=str('test'), Price = 30, Inventory=10)
        print('items are',MenuItem.objects.all())
        self.assertEqual(item.Title, str("test"))