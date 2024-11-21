from django.db import models

# Create your models here.
from django.db import models  

class User(models.Model):  
    username = models.CharField(max_length=80)  
    password = models.CharField(max_length=120)  
    active = models.BooleanField(default=True)  

    def __str__(self):  
        return self.username