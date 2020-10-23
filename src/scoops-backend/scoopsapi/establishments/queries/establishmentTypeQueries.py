import graphene
from graphene_django import DjangoObjectType

from establishments.models import EstablishmentType

class EstablishmentTypeType(DjangoObjectType):
    class Meta:
        model = EstablishmentType
        