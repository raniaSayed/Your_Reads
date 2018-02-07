from django.db import models

class Authors(models.Model):
    author_name = models.CharField(max_length= 100)
    author_nationality = models.CharField(max_length= 100)
    born_at=models.DateField(null=True, blank=True)
    died_at=models.DateField(null=True, blank=True)
    contacts= models.TextField(max_length=200)
    bio= models.CharField(max_length=200)
    image = models.FileField(null=True,blank=True)
