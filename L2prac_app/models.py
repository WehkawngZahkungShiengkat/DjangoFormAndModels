from django.db import models
import uuid

# Create your models here.
class Uinfo(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=264,unique=False)
    lname = models.CharField(max_length=264,unique=False)
    umail = models.EmailField(unique=True)

    def __str__(self):
        return (self.fname+" "+self.lname)
