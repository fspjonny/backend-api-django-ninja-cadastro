from django.contrib.auth.models import User
from django.test import Client, TestCase
from rest_framework import status


class AccountsAPITest(TestCase):
    
    def setUp(self, *args, **kwargs):
        self.client = Client()
        self.usertest = User.objects.create_user(username='usertest',email='userteste@email.com', password='teste1Master')
        return super().setUp(*args, **kwargs)
    

    def test_url_logon_api_accounts(self):
        response = self.client.get('/accounts/api/v1/logon/', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

