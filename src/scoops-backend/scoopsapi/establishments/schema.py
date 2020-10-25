from graphene import ObjectType, List, String, ID, Field
from django.shortcuts import get_object_or_404
from establishments.models import EstablishmentTypes
from djongo.models import ObjectIdField
from bson.objectid import ObjectId
from graphql_jwt.decorators import login_required

class EstablishTypeSchema(ObjectType):
    _id = ID()
    name = String()


class EstablishmentSchema(ObjectType):
    establishment_types = List(EstablishTypeSchema)
    establishment_type = Field(EstablishTypeSchema, typeId=ID())
    
    def resolve_establishment_types(root, info, **kwargs):
        return EstablishmentTypes.objects.all()

    @login_required
    def resolve_establishment_type(root, info, typeId):
        try:
            _type = EstablishmentTypes.objects.get(pk=ObjectId(typeId))
            
        except EstablishmentTypes.DoesNotExist:
            _type = None
        return _type