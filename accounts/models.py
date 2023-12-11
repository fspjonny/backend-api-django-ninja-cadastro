from django.contrib.auth.models import User
from django.db import models


class ClientAccountToken(models.Model):
    
    class Meta:
        verbose_name='Cliente Token'
        verbose_name_plural='Clientes Tokens'
    
    username = models.ForeignKey(User, on_delete=models.CASCADE)    
    refresh_token = models.CharField(blank=True, max_length=300, verbose_name='Refresh Token')
    access_token = models.CharField(blank=True, max_length=300, verbose_name='Access Token')
    date = models.DateField(null=True, verbose_name='Criado em')
    
    def __str__(self) -> str:
        return f'{self.username}, {self.refresh_token}, {self.access_token}, {self.date}'
        