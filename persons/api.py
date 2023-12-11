from typing import List, Optional

from ninja.pagination import paginate
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

from persons.models import PersonsModel
from persons.paginator import PersonPageNumberPagination
from persons.schema import AllPersonSchema, NotFoundSchema, PersonSchema

api = NinjaExtraAPI(csrf=False)
api.title="Persons API"
api.register_controllers(NinjaJWTDefaultController)


@api.get("persons/", response=List[AllPersonSchema], auth=JWTAuth())
@paginate(PersonPageNumberPagination)
def list_all_persons(request, name: Optional[str] = None):
    if name:
        return PersonsModel.objects.filter(nome__iregex=f'^{name}')
    return PersonsModel.objects.all()


@api.get("persons/{person_id}", response={200: List[AllPersonSchema], 404: NotFoundSchema}, auth=JWTAuth())
@paginate(PersonPageNumberPagination)
def get_person_by_id(request, person_id: int):
    try:
        person = PersonsModel.objects.get(pk=person_id)
        return [person]
    except PersonsModel.DoesNotExist as err:
        return 404, {"message":f"Person with id:{person_id}, does not exist!"}


@api.post("persons/", response={201: PersonSchema}, auth=JWTAuth())
def create_new_person(request, person: PersonSchema):
    person = PersonsModel.objects.create(**person.dict())
    return person


@api.put("persons/{person_id}", response={200: PersonSchema, 404: NotFoundSchema}, auth=JWTAuth())
def update_a_person(request, person_id: int, data: PersonSchema):
    try:
        person = PersonsModel.objects.get(pk=person_id)
        for attribute, value in data.dict().items():
            setattr(person, attribute, value)
        person.save()
        return 200, person    
    except PersonsModel.DoesNotExist as err:
        return 404, {"message":f"Person with id:{person_id}, does not exist!"}


@api.delete("persons/{person_id}", response={200: None, 404: NotFoundSchema}, auth=JWTAuth())
def delete_a_person(request, person_id: int):
    try:
        person = PersonsModel.objects.get(pk=person_id)
        person.delete()
        return 200
    except PersonsModel.DoesNotExist as err:
        return 404, {"message":f"Person with id:{person_id}, does not exist!"}
