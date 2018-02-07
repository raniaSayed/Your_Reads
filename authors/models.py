from django.db import models
import datetime
# Create your models here.
class Authors(models.Model):
    author_name = models.CharField(max_length= 100)
    author_nationality = models.CharField(max_length= 100)
    # published_at = models.DateField()
    # born_at=models.DateField(null=True, blank=True)
    # died_at=models.DateField(null=True, blank=True)
    contacts= models.CharField(max_length=200)
    bio= models.CharField(max_length=200)


    # def __str__(self):
    #     return self.title
