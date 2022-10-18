import mailbox
from unicodedata import name
from django.db import models

# Create your models here.
class New(models.Model):
    tittle = models.CharField(max_length=20)
    body = models.CharField(max_length=120)
    creation_date = models.DateField()
    owner_first_name = models.CharField(max_length=16)
    owner_last_name = models.CharField(max_length=16)
    collaborators = models.IntegerField()

class Contact(models.Model):
    name=models.CharField(max_length=20)
    mail=models.EmailField()
    message=models.CharField(max_length=200)