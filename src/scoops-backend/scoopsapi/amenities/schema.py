from amenities.models import AmenityType, Amenities
from graphene import ObjectType, List, Field, String, Mutation, ID
from scoopsapi.helpers.baseType import BaseType
from graphql_jwt.decorators import superuser_required

class AmenityTypeSchema(ObjectType):
    name = String()

class AmenitySchema(BaseType):
    _id = ID()
    name = String()
    amenityType = Field(AmenityTypeSchema)


class AmenityQueries(ObjectType):
    AmenityTypes = List(AmenityTypeSchema)


    def resolve_amenityTypes(root, info, **kwargs):
        return AmenityType.objects.all()


# Mutations

class CreateAmenity(Mutation):
    class Arguments:
        name = String()
        amenityType = String()
        
    amenity = Field(AmenitySchema)

    @superuser_required
    def mutate(root, info, name, amenityType):
        newAmenity = Amenities(name=name)
        newAmenity.amenityType = { 'name' : amenityType }  
        newAmenity.save()
        return CreateAmenity(amenity=newAmenity)

class AmenityMutations(ObjectType):
    create_amenity = CreateAmenity.Field()





    