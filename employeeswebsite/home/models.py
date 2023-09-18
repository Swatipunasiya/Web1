from django.db import models

# Create your models here.
class Mymodel(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField()
    image=models.ImageField(upload_to='static/media')