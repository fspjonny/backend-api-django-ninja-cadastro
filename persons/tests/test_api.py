import json

from django.contrib.auth.models import User
from django.test import Client, TestCase
from ninja_jwt.tokens import RefreshToken
from rest_framework import status

from persons.models import PersonsModel


class PersonsAPITest(TestCase):
    
    def setUp(self, *args, **kwargs):
        self.client = Client()
        self.new_person = PersonsModel.objects.create(
            pai = 'Arnaldo Gonçalves dos Santos',
            mae = 'Therezha Maria dos Santos',
            nome = 'Helenna Maria Gonçalves do Santos',
            sexo = 'M',
            nascimento = '1980-06-11',
            rg = '687541148',
            cpf = '04578213652',
            email = 'helena.g.santos@email.com.br',
            telefone = '934567731',
            endereco = 'Rua Piratininga, 12 apt: 202',
            cargo = 'Analista Financeira',
            salario = '2347.50',
            admissao = '2019-05-01',
        )
        self.usertest = User.objects.create_user('usertest','teste1Master')
        self.user_token = RefreshToken.for_user(self.usertest)

        return super().setUp(*args, **kwargs)
    

    def test_url_list_all_persons(self):
        response = self.client.get('/api/v1/persons', follow=True)
        self.assertEqual(response.status_code, 200)


    def test_url_persons_by_id(self):
        token = self.user_token.access_token
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}',}
        person_id = self.new_person.id
        response = self.client.get(f'/api/v1/persons/{person_id}', **headers, follow=True)
        self.assertEqual(response.status_code, 200)


    def test_url_create_new_person(self):
        token = self.user_token.access_token
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        
        person_data = {
            'nome':'Juliana Torres',
            'sexo':'M',
            'nascimento':'1980-06-11',
            'pai':'José Aguinaldo Torres',
            'mae':'Ana Clara Torres',
            'rg':'687541148',
            'cpf':'04555213652',
            'email':'juliana.torres@email.com',
            'telefone':'934567731',
            'endereco':'Rua Planaltina, 22 apt: 2026',
            'cargo':'Contadora',
            'salario':'2347.50',
            'admissao':'2019-05-01',
        }
        
        response = self.client.post('/api/v1/persons/', json.dumps(person_data), content_type='application/json', **headers, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




    def test_url_update_person(self):
        token = self.user_token.access_token
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        
        novo_cargo = 'Advogada'
        
        self.new_person.cargo = novo_cargo
        updated_data = self.new_person
        
        data = {
            'nome':updated_data.nome,
            'sexo': updated_data.sexo,
            'nascimento': updated_data.nascimento,
            'pai': updated_data.pai,
            'mae': updated_data.mae,
            'rg': updated_data.rg,
            'cpf': updated_data.cpf,
            'email': updated_data.email,
            'telefone': updated_data.telefone,
            'endereco': updated_data.endereco,
            'cargo': updated_data.cargo,
            'salario': updated_data.salario,
            'admissao': updated_data.admissao,
        }
       
        response = self.client.put(f'/api/v1/persons/{self.new_person.id}', json.dumps(data), content_type='application/json', **headers, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        cargo_modificado = json.loads(response.content)
        self.assertEqual(cargo_modificado['cargo'], novo_cargo)

        
    def test_url_delete_person(self):
        token = self.user_token.access_token
        headers = {'HTTP_AUTHORIZATION': f'Bearer {token}'}
        
        id_existing_person=1
        id_not_existing_person=50
        
        response = self.client.delete(f'/api/v1/persons/{id_existing_person}', **headers, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(f'/api/v1/persons/{id_not_existing_person}', **headers, follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
