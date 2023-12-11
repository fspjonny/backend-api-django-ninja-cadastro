from typing import Any, List

from django.db.models import QuerySet
from ninja import Field, Schema
from ninja.conf import settings
from ninja.pagination import PaginationBase


class PersonPaginationBase(PaginationBase):
    class Output(Schema):
        items: List[Any]
        count: int


class PersonPageNumberPagination(PersonPaginationBase):
    class Output(Schema):
        items: List[Any]
        count: int
        per_page: int
    
    class Input(Schema):
        page: int = Field(1, ge=1)

    def __init__(
        self, 
        page_size: int = settings.PAGINATION_PER_PAGE, 
        **kwargs: Any) -> None:
        
        self.page_size = page_size
        super().__init__(**kwargs)

    def paginate_queryset(self, queryset: QuerySet, pagination: Input, **params: Any) -> Any:
        offset = (pagination.page - 1) * self.page_size
        
        return {
            "items": queryset[offset : offset + self.page_size],
            "count": self._items_count(queryset),
            "per_page": self.page_size
        }  
        
