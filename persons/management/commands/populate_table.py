from django.core.management.base import BaseCommand

from mock.create_fake_persons import get_person
from persons.models import PersonsModel
from utils.progressbar import progressbar


def create_persons():
    list_of_persons = []
    
    for _ in progressbar(range(100), 'Pessoas'):
        data = get_person()
        obj = PersonsModel(**data)
        list_of_persons.append(obj)
    PersonsModel.objects.bulk_create(list_of_persons)

class Command(BaseCommand):
    help = "Criar Pessoas no cadastro"

    def handle(self, *args, **options):
        create_persons()
