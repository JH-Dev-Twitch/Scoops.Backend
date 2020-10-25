from djongo import models

# Create your models here.

class EstablishmentTypes(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=120)
    
    class Meta:
        db_table = "establishment_types"

