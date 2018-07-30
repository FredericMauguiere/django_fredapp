from django.test import TestCase
from .models import CatalogItem
from django.urls import reverse

class CatalogItemModelTests(TestCase):
    def setUp(self):
        CatalogItem.objects.create(name='just a test')

    def test_name(self):
        item=CatalogItem.objects.get(id=1)
        expected_object_name = f'{item.name}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase):
    def setUp(self):
        CatalogItem.objects.create(name='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')