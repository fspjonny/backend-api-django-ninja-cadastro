from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

WIDGET_CLASS = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'

class RecoverForm(forms.ModelForm):
    
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
        validators=[],
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
        validators=[],
        label='Confirmar senha',
    )
    
    class Meta:
        model= User
        
        fields= [
            'email',
            'password',
        ]

            
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class':WIDGET_CLASS,
                    'placeholder':'Seu email de cadastro',
                    'required':True,
                }
            )
        }


# VALIDAÇÃO DE CAMPOS

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        
        clean_data= self.cleaned_data
        
        email= clean_data.get('email')
        password= clean_data.get('password')
        password_confirm= clean_data.get('password_confirm')
        

        email_exists= User.objects.filter(email=email).exists()
        if not email_exists:
            self.listerrors['email'].append('E-mail não existe no cadastrado!')
        
        if password != password_confirm:
            self.listerrors['password'].append('Senhas digitadas são diferentes!')
            self.listerrors['password_confirm'].append('Senhas digitadas são diferentes!')

        if self.listerrors:
            raise ValidationError(self.listerrors)
        
        return super_clean
        
