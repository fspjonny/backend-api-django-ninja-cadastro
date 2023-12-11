from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.forms.login_form import LoginForm
from accounts.models import ClientAccountToken


def login_form(request):
    user_data_form = LoginForm()
    return render(request, 'accounts/userlogin.html',{'user_data_form':user_data_form})


def verify_user(request):
    if not request.POST:
        return redirect('accounts:login')
    
    login_data = LoginForm(request.POST)

    if login_data.is_valid():
        authenticated_user= authenticate(
            username=login_data.cleaned_data.get('username',''),
            password=login_data.cleaned_data.get('password',''),
        )

        if authenticated_user is not None:
            login(request, authenticated_user)
        else:
            messages.error(request, 'Dados incorretos!')
    else:
        messages.error(request, 'Dados incorretos!')
    return redirect('accounts:login')


@login_required(login_url='accounts:login', redirect_field_name='next')
def logout_user(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login', redirect_field_name='next')
def painel_cliente(request):
    # Se usuário já tiver Token ativo ou não serão exibidos os dados.
    try:
        user_token = ClientAccountToken.objects.filter(username=request.user).first()
       
        if user_token:
            expirado=False
            validade = date.today()
            expirado = True if validade != user_token.date else False
            return render(request, 'accounts/clientes.html', {'user_token':user_token, 'expirado':expirado})
        return render(request, 'accounts/clientes.html')
    
    # Se o usuário não possuir Token a tela será exibida possibilitará criar chaves.
    except ClientAccountToken.DoesNotExist:
        return render(request, 'accounts/clientes.html')
    