# Backend API Django Ninja - Cadastro de Profissionais

É uma API em **Django Ninja** para um cadastro de profissionais prestadores de serviços.

_*Para esta versão do aplicativo, tive que modificar o banco de dados(Originalmente PostreSQL) para o Sqlite3 por causa do local de hospedagem escolhido(PythonAnywhere que não dá suporte grátis ao PostgreSQL), uma vez que o Heroku também acabou com a hospedagem gratuita com PostgreSQL.*_

### Para ver este APP funcionando na internet acesse:

### http://url.pythonanywhere.com/

<br/>
<div align="center">
<img height="600" src="https://i.imgur.com/I6GPwFp.png" alt="Tela Inicial">
</div>

## Este projeto foi feito com:

- [Python 3.11.4](https://docs.pytest.org/en/7.4.x/)
- [Pytest 7.4.2](https://docs.pytest.org/en/7.4.x/)
- [Pytest Django 4.5.2](https://pytest-django.readthedocs.io/en/latest/)
- [Django Ninja 0.22.2](https://django-ninja.dev/)
- [Django Jazzmin 2.6.0](https://django-jazzmin.readthedocs.io/)
- [Django Cors Headers 4.2.0](https://pypi.org/project/django-cors-headers/)
- [Faker 19.3.0](https://faker.readthedocs.io/en/master/)
- [Tailwind CSS 3.3.6 CDN](https://cdn.tailwindcss.com)

## Como rodar o projeto?

- Clone esse repositório. `git clone https://github.com/fspjonny/backend-api-django-ninja-cadastro`
- Crie uma virtualenv com Python 3.11.4 no mínimo.
- Ative sua virtualenv.
- Instale as dependências listadas em requirements.txt.
- Rode as migrações.
- Configure seu .env(exemplo em .env_example)
  ### - Gerar uma Key para o .env
- Execute o comando: `python manage.py generate_key`
- Salve a chave gerada no seu arquivo .env
  ### - Popular a tabela com o Faker
- Execute o comando: `python manage.py populate_table`

### Comandos:

cd backend-api-django-ninja-cadastro<br>
python -m venv venv<br>
pip install -r requirements.txt<br>
python manage.py migrate<br>
python manage.py runserver<br>
