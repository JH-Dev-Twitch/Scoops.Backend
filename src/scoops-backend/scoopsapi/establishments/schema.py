import graphene
from graphene_django import DjangoObjectType
from establishments.models import EstablishmentType
from establishments.queries.establishmentTypeQueries import EstablishmentTypeType


        
class EstablishmentQuerySchema(graphene.ObjectType):
    get_all_types = graphene.List(EstablishmentTypeType)

