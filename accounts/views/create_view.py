from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

from accounts.forms.form_create import RegisterForm


def create_form(request):
    register_data = request.session.get('register_form_data', None)
    
    create_user_form = RegisterForm(register_data)
    return render(request, 'accounts/create.html',{'create_user_form':create_user_form})

def receive_form(request):
    if not request.POST:
        del(request.session['register_form_data'])
        return redirect('accounts:create')
    
    POST_DATA = request.POST
    request.session['register_form_data'] = POST_DATA
    form = RegisterForm(POST_DATA)
    
    if form.is_valid():
        data = form.save(commit=False)
        data.username = data.username.lower()
        data.first_name = data.first_name.capitalize()
        data.email = data.email.lower()
        data.password = make_password(data.password)
        
        form.save(commit=True) #commit=False não salva dados
        del(request.session['register_form_data'])
        messages.success(request, 'Conta criada com sucesso!')
    
    return redirect('accounts:create')
