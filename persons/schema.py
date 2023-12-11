from ninja import ModelSchema, Schema

from persons.models import PersonsModel


class PersonSchema(ModelSchema):
    class Config:
        model = PersonsModel
        model_fields = ['nome','sexo','nascimento','pai','mae','rg',
                        'cpf','email','telefone','endereco','cargo','salario','admissao',
                        ]

class AllPersonSchema(ModelSchema):
    class Config:
        model = PersonsModel
        model_fields = ['id','nome','sexo','nascimento','pai','mae','rg','cpf',
                        'email','telefone','endereco','cargo','salario','admissao']

class NotFoundSchema(Schema):
    message: str
