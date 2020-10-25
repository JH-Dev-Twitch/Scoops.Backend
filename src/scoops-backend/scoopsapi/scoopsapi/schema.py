from graphene import ObjectType, Schema
from amenities.schema import AmenityQueries, AmenityMutations
from establishments.schema import EstablishmentSchema
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class AuthMutation(ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   refresh_token = mutations.RefreshToken.Field()

class Query(AmenityQueries, EstablishmentSchema):
   pass

class Mutation(AmenityMutations,AuthMutation):
   pass

schema = Schema(query=Query, mutation=Mutation)