from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname=models.CharField(max_length=256)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()