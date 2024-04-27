from django.db import models

# Create your models here.
class Freefire(models.Model):
    name = models.CharField( max_length=50)
    cls = models.CharField( max_length=50)
    def __str__(self):
        return self.name
    