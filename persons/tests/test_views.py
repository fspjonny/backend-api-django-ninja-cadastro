from django.test import TestCase
from django.test.client import Client
from django.urls import resolve, reverse

from persons.views import initial


class PersonsViewsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        
    def test_whether_executed_method_is_initial(self):
        view = resolve(reverse('persons:initial'))
        self.assertIs(view.func, initial)


    def test_if_wrong_url_make_the_redirect_route_status302_occours(self):
        invalid_url = '/url_inexistente/'
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 302)
        