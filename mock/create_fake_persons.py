from datetime import date

from faker import Faker

fake = Faker('pt-BR')

def pessoa(pai, mae):
    escolha = fake.random_int(min=1, max=2)
    sexo=''
    
    if escolha == 1:
        nome = fake.first_name_male()
        sexo = 'Masculino'
    else:
        nome = fake.first_name_female()
        sexo = 'Feminino'
    
    nome_pai = pai.split()
    pai_sobrenome = " ".join(nome_pai[1:])

    nome_mae = mae.split()
    mae_sobrenome = " ".join(nome_mae[1:])
    
    return f'{nome} {pai_sobrenome} {mae_sobrenome}', sexo


def generate_email(usuario):
    lista = usuario.split()
    nome = lista[0].lower()
    corpo = lista[-1].lower()
    return f'{nome}.{corpo}@{fake.free_email_domain()}'



def get_person():
    pai = f'{fake.first_name_male()} {fake.last_name()}'
    mae = f'{fake.first_name_female()} {fake.last_name()}'
    nome, sexo = pessoa(mae, pai)
    nascimento = fake.date_between(date(1960, 1, 1))
    rg = fake.random_number(digits=9, fix_len=True) 
    cpf = fake.random_number(digits=11, fix_len=True) 
    email = generate_email(nome)
    telefone = f'9{fake.random_number(digits=8, fix_len=True)}' 
    endereco = fake.address()
    cargo = fake.job()
    salario = f'{fake.random_number(digits=4)}.{fake.random_number(digits=2, fix_len=True)}'
    admissao = fake.date_between(date(1980, 1, 1))
    
    data = dict(
        pai = pai,
        mae = mae,
        nome = nome,
        sexo = sexo,
        nascimento = nascimento,
        rg = rg,
        cpf = cpf,
        email = email,
        telefone = telefone,
        endereco = endereco,
        cargo = cargo,
        salario = salario,
        admissao = admissao,
    )
    return data
