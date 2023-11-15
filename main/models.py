from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50) 
    isBandMember = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name