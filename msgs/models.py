from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Msg(models.Model):
    msg_send = models.CharField(max_length=240)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    