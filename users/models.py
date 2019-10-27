from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Files(models.Model):
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   # file = models.FileField('/uploads')
    file = models.FileField(upload_to='docs')
