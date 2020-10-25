from djongo.models import Model, ObjectIdField

class BaseModel(Model):
    _id = ObjectIdField()