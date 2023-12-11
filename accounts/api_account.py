from django.contrib.auth import authenticate
from ninja import NinjaAPI, Schema
from ninja.errors import HttpError

from accounts.models import ClientAccountToken

api_auth = NinjaAPI(urls_namespace="account api")
api_auth.title="Persons API"

class LogonSchema(Schema):
    username:str
    password:str

@api_auth.post("logon/", response={ 200 : dict })
def logon_account(request, data: LogonSchema):
    
    username = data.username
    password = data.password
    
    # Faz a autenticação do usuário    
    authentic_user = authenticate(username=username, password=password)

    # Se não retornar None é porque o usuário é válido e está autenticado.
    if authentic_user is not None:
        user_data = ClientAccountToken.objects.filter(username__username=authentic_user.get_username()).first()
        
        # O usuário existe e está autenticado, mas ainda não criou um token de acesso.
        if user_data is None:
            raise HttpError(status_code=202, message='202')
        
        # O usuário está autenticado e já tem token de acesso.
        list_data = str(user_data).replace(',','').split()
        return {
            "first_name":authentic_user.first_name, 
            "username":list_data[0],
            "refresh_token":list_data[1],
            "access_token":list_data[2],
            "created_at":list_data[3]
            }
    else: # Se o usuário não existir ou estiver incorreto.
        raise HttpError(status_code=400, message="Usuário incorreto!")
    