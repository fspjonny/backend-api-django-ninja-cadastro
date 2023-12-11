from django.urls import path

from .views import initial

app_name='persons'

urlpatterns = [
    path('', initial, name='initial'),
]
