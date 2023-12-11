from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key


def generate_key():
    print(80*'-')
    print('\n')
    print(f'Chave: {get_random_secret_key()}\n')
    print(80*'-')
    
class Command(BaseCommand):
    help = "Gerar chaves para Django e JWT"

    def handle(self, *args, **options):
        generate_key()
