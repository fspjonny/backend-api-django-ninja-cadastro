import re
from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

WIDGET_CLASS = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'

def strongPasword(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')
    
    if not regex.match(password):
        raise ValidationError(('Digite pelo menos 8 caracteres entre letras maiúsculas e minúsculas e números.'),
                              code='Inválido')
    

class RegisterForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.listerrors= defaultdict(list)
    
    
    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class':WIDGET_CLASS,
                'placeholder':'Digite uma senha forte',
                'minlength':8,
                'type':'password',
            }
        ),
        validators=[strongPasword],
        label='Senha',
    )
    
    password_confirm = forms.CharField(
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class':WIDGET_CLASS,
                'placeholder':'Repita a senha digitada',
                'minlength':8,    
                'type':'password',
            }
        ),
        validators=[strongPasword],
        label='Confirmar senha',
    )
    
    class Meta:
        model= User
        
        fields= [
            'username',
            'first_name',
            'email',
            'password',
        ]
       

            
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class':WIDGET_CLASS,
                    'placeholder':'Crie seu nome de usuário',
                    'minlength':3,
                    'required':True,
                }
            ),
            
            'first_name': forms.TextInput(
                attrs={
                    'class':WIDGET_CLASS,
                    'placeholder':'Seu nome',
                    'minlength':3,
                    'required':True,
                }
            ),
           
            'email': forms.EmailInput(
                attrs={
                    'class':WIDGET_CLASS,
                    'placeholder':'Seu email',
                    'required':True,
                }
            )
        }


# VALIDAÇÃO DE CAMPOS

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        
        clean_data= self.cleaned_data
        
        newuser= clean_data.get('username')
        name= clean_data.get('first_name')
        email= clean_data.get('email')
        password= clean_data.get('password')
        password_confirm= clean_data.get('password_confirm')
        
        user_exists= User.objects.filter(username=str(newuser).lower()).exists()
        if user_exists:
            self.listerrors['username'].append('Usuário já está cadastrado!')
        elif len(newuser) < 3:
            self.listerrors['username'].append('Nomes de usuário devem ter 3 ou mais caracteres')
        
        if len(name) < 3:
            self.listerrors['name'].append('Primeiro nome deve ter 3 ou mais caracteres')

        email_exists= User.objects.filter(email=str(email).lower()).exists()
        if email_exists:
            self.listerrors['email'].append('E-mail já está cadastrado!')
        
        if password != password_confirm:
            self.listerrors['password'].append('Senhas digitadas são diferentes!')
            self.listerrors['password_confirm'].append('Senhas digitadas são diferentes!')

        if self.listerrors:
            raise ValidationError(self.listerrors)
        
        return super_clean
        
