from django.urls import path

from accounts.views.create_view import create_form, receive_form
from accounts.views.jwt_token import make_tokens_for_user
from accounts.views.login_view import (login_form, logout_user, painel_cliente,
                                       verify_user)
from accounts.views.recover_view import proccess_recovery, recover_view

app_name='accounts'

urlpatterns = [
    path('', login_form, name='login'),
    path('login/', verify_user, name='verify_login'),
    path('create/', create_form, name='create'),
    path('create/client/', receive_form, name='create_client'),
    path('recover/pass/', recover_view, name='recovery'),
    path('change/pass/', proccess_recovery, name='change_pass'),
    path('logout/', logout_user, name='logout'),
    path('client/', painel_cliente, name='client'),
    path('cliente/pair', make_tokens_for_user, name='make_tokens'),
]
