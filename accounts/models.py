from django.db import models
from django.contrib.auth.models import User
from datetime import date

class ExtendUser(models.Model):
    avatar = models.ImageField(upload_to='avatars/',null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.avatar} {self.birthday}'
    
    @property
    def age(self):
        if self.birthday:
            today = date.today()
            age = today.year - self.birthday.year - (
                    (today.month, today.day) < (self.birthday.month, self.birthday.day))
            return age
        return 0