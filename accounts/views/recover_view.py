from django.contrib import messages
from django.shortcuts import redirect, render

from accounts.forms.form_recover import RecoverForm


def recover_view(request):
    recover_pass_data = request.session.get('recover_pass', None)
    
    recover_form = RecoverForm(recover_pass_data)    
    return render(request, 'accounts/recover.html',{'recover_form':recover_form})

def proccess_recovery(request):
    if not request.POST:
        del(request.session['recover_pass'])
        return redirect('accounts:recovery')
    
    POST_DATA = request.POST
    request.session['recover_pass'] = POST_DATA
    form = RecoverForm(POST_DATA)
    
    if form.is_valid():
        form.save(commit=True) #commit=False não salva dados
        del(request.session['recover_pass'])
        messages.success(request, 'Senha alterada com sucesso!')
    
    return redirect('accounts:recovery')    
