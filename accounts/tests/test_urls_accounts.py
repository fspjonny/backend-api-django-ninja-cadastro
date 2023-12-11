from django.test import TestCase
from django.urls import resolve, reverse


class AccountsUrlsTest(TestCase):
    
    def test_url_if_goto_login(self):
        url = resolve(reverse('accounts:login',))
        self.assertEqual(url.route, 'account/')
        self.assertEqual(url.url_name, 'login')

    def test_url_if_goto_create(self):
        url = resolve(reverse('accounts:create',))
        self.assertEqual(url.route, 'account/create/')
        self.assertEqual(url.url_name, 'create')

    def test_url_if_goto_create_client(self):
        url = resolve(reverse('accounts:create_client',))
        self.assertEqual(url.route, 'account/create/client/')
        self.assertEqual(url.url_name, 'create_client')

    def test_url_if_goto_recovery(self):
        url = resolve(reverse('accounts:recovery',))
        self.assertEqual(url.route, 'account/recover/pass/')
        self.assertEqual(url.url_name, 'recovery')

    def test_url_if_goto_change_password(self):
        url = resolve(reverse('accounts:change_pass',))
        self.assertEqual(url.route, 'account/change/pass/')
        self.assertEqual(url.url_name, 'change_pass')

    def test_url_if_goto_logout(self):
        url = resolve(reverse('accounts:logout',))
        self.assertEqual(url.route, 'account/logout/')
        self.assertEqual(url.url_name, 'logout')

    def test_url_if_goto_client_painel(self):
        url = resolve(reverse('accounts:cliente',))
        self.assertEqual(url.route, 'account/cliente/')
        self.assertEqual(url.url_name, 'cliente')

    def test_url_if_goto_client_make_tokens(self):
        url = resolve(reverse('accounts:make_tokens',))
        self.assertEqual(url.route, 'account/cliente/pair')
        self.assertEqual(url.url_name, 'make_tokens')
