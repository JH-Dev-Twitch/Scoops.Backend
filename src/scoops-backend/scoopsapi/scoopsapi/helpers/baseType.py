from graphene import ObjectType, ID


class BaseType(ObjectType):
    _id = ID()