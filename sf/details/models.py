from django.db import models

# Create your models here.

class Contect(models.Model):
    user=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50, default="")
    sem=models.CharField(max_length=50, default="")
    phone=models.CharField(max_length=50, default="")
    email=models.CharField(max_length=50, default="")
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name