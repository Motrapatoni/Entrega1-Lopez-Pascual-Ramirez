from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class New(models.Model):
    tittle = models.CharField(max_length=25)
    body = RichTextField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    owner_name = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    
    def __str__(self):
        return self.tittle


class Contact(models.Model):
    name=models.CharField(max_length=20)
    mail=models.EmailField()
    message=models.CharField(max_length=200)
    
    def __str__(self):
        return f'Name: {self.name} - Mail: {self.mail}'