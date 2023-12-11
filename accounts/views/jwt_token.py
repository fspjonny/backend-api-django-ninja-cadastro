from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from ninja_jwt.tokens import RefreshToken

from accounts.models import ClientAccountToken


@login_required(login_url='accounts:login', redirect_field_name='next')
def make_tokens_for_user(request):
    
    # Vai tentar atualizar a chave de API se o suário já possuir uma chave anterior vencida.
    try:
        refresh = RefreshToken.for_user(request.user)
        
        client = ClientAccountToken.objects.get(username=request.user)
        client.refresh_token = refresh
        client.access_token = refresh.access_token
        client.date = date.today()
        client.save()
        
        messages.success(request, 'Chave atualizada com sucesso!')
        return redirect('accounts:cliente')
    
    # Caso contrário se for o primeiro acesso, vai criar um par de chaves de acesso a API
    except ClientAccountToken.DoesNotExist:
        newToken = RefreshToken.for_user(request.user)
        newclient = ClientAccountToken()
        newclient.username = request.user
        newclient.refresh_token = newToken
        newclient.access_token = newToken.access_token
        newclient.date = date.today()
        newclient.save()

        messages.success(request, 'Token criado com sucesso!')
        return redirect('accounts:cliente')

    
    
