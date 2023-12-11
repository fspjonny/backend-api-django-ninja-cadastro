from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import resolve, reverse
from rest_framework import status

from accounts.forms.form_create import RegisterForm
from accounts.views.create_view import create_form


class AccountsViewCreateTest(TestCase):
    
    form = RegisterForm()
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
            
            
    def test_if_call_correct_method_create_form(self):
        view = resolve(reverse('accounts:create'))
        
        # if correct method's name is create_from
        self.assertIs(view.func, create_form)


    def test_if_create_user_and_loads_correct_template(self):
        url = reverse('accounts:create')
        
        self.client.post(url, data=self.form_data, follow=True)
        
        response = self.client.post(url, data=self.form_data, follow=True)
        
        # if create a new user, status is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # the correct template name's is create.html
        self.assertTemplateUsed(response,'accounts/create.html')
    
    
    def test_if_created_user_is_not_a_admin(self):
        # create and save a new user
        user= User.objects.create_user(
            username=self.form_data['username'], 
            first_name=self.form_data['first_name'], 
            email=self.form_data['email'], 
            password=self.form_data['password'], 
            )
        user.save()
        
        url = reverse('accounts:create')
        
        # send username and password to try login with new user
        self.client.post(url, data=({'username':'usertest', 'password':'#teste1Master'}), follow=True)

        # try authenticated with new user
        authenticated_user= authenticate(username='usertest', password='#teste1Master')
        
        # if new user is authenticated, must have True
        self.assertIs(authenticated_user.is_authenticated, True)
        
        # if new user is not a superuser, must have False
        self.assertIs(authenticated_user.is_superuser, False)

    def test_if_receive_form_receive_all_valid_info(self):
        # Instance form receive data from new user form_data
        form = RegisterForm(self.form_data)
        
        # if all data is valid, must have True
        response = form.is_valid()
        self.assertTrue(response)
