from django.contrib import admin
from django.urls import include, path

from accounts.api_account import api_auth
from persons.api import api

urlpatterns = [
    path('manutencao/', admin.site.urls),
    path('', include('persons.urls'), name='inicio'),
    path('account/', include('accounts.urls'), name='login'),
    path('account/api/v1/', api_auth.urls),
    path('api/v1/', api.urls),
]

handler404 = "persons.views.handler404"
