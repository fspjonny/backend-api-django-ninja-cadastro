from django import forms

WIDGET_CLASS = 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5'

class LoginForm(forms.Form):
       
    username= forms.CharField(
        required=True,
        widget= forms.TextInput(
            attrs={
                'class':WIDGET_CLASS,
                'placeholder':'Usuário',
            }
        )
    )
    
    password= forms.CharField(
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class':WIDGET_CLASS,
                'placeholder':'**********',
            }
        )
    )
    
