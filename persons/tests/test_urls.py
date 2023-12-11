from django.test import TestCase
from django.urls import reverse


class PersonsUrlTest(TestCase):
    
    def test_reverse_url_if_goto_home(self):
        home_url = reverse('persons:initial')
        self.assertEqual(home_url, '/')
