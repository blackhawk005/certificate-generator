from django.conf import settings
from django.db import models

# Create your models here.

class Detail(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    organizer_name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200)
    description = models.TextField()
    certificate_class = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(self.name)