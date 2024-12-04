from django.db import models

# Create your models here.
class FileFormUpload(models.Model):
    name=models.CharField(max_length=256)
    file=models.FileField(upload_to="uploads/")