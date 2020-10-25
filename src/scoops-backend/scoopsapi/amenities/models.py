from djongo import models

# Create your models here.
class AmenityType(models.Model):
    name = models.CharField(max_length=200)


    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Amenities(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    amenityType = models.EmbeddedField(model_container=AmenityType)
    
    class Meta:
        db_table='amenities'

    def __str__(self):
        return self.name
