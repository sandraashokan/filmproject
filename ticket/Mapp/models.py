from django.db import models

# Create your models here.
class movie(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    img=models.ImageField(upload_to=None,null=True,blank=True)

class update(models.Model):
    title=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    img=models.ImageField(upload_to='update/img')
