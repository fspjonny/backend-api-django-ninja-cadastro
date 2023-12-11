from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from rest_framework import status

from accounts.forms.login_form import LoginForm


class AccountsViewLoginTest(TestCase):
    
    client = Client()
    
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username':'usertest',
            'first_name':'Tester',
            'email':'test.user@email.com.br',
            'password':'#teste1Master',
            'password_confirm':'#teste1Master',
        }
        return super().setUp(*args, **kwargs)
            
            
    def test_if_loads_correct_template_for_login_form(self):
        url= reverse('accounts:login')
        # make a request post for url and view for send data off login form.
        response = self.client.post(url, data=self.form_data, follow=True)
        # the correct loads template must be userlogin.html
        self.assertTemplateUsed(response, 'accounts/userlogin.html')

    def test_for_verify_if_user_and_pass_is_valid_account(self):
        user = User.objects.create_user(
            self.form_data['username'],
            self.form_data['email'],
            self.form_data['password']
        )
        user.save()
        
        url= reverse('accounts:verify_login')
        
        # form receive user and password to send for validation
        form = LoginForm(
            data=(
                {'username':self.form_data['username'], 
                 'password':self.form_data['password']
                }
            )
        )
        # send data for verify validation
        self.client.post(url, data=form.data, follow=True)
        valid = form.is_valid()
        # if valid, result must be True
        self.assertTrue(valid)
        
        # make user authenticated
        user_authenticated = authenticate(
            username=self.form_data['username'],
            password=self.form_data['password']
        )
        # if can authorization, result must be True
        self.assertIs(user_authenticated.is_authenticated, True)


    def test_if_user_make_logout_and_redirect(self):
        url = reverse('accounts:logout')
        response = self.client.get(url, follow=True, secure=True)
        
        # if logout, redirect to login page
        self.assertEqual(response.resolver_match.url_name, 'login')
        # if status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
