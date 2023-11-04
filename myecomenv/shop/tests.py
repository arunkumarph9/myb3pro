from django.test import TestCase
from django.urls import resolve, reverse
from .views import base,cart


class TestURL(TestCase):
    def test_urlbase(self):
        url = reverse('home')
        print("url is: ", url)
        print("Resolve: ", resolve(url))
        self.assertEqual(resolve(url).func, base)


class TestURL(TestCase):
    def test_urlcart(self):
        url = reverse('cart')
        print("url is: ", url)
        print("Resolve: ", resolve(url))
        self.assertEqual(resolve(url).func, cart)



# Create your tests here.
