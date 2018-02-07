from django.db import models
<<<<<<< HEAD
#
class Authors(models.Model):
    author_name = models.CharField(max_length= 100)
    author_nationality = models.CharField(max_length= 100)
    born_at=models.DateField(null=True, blank=True)
    died_at=models.DateField(null=True, blank=True)
    contacts= models.TextField(max_length=200)
    bio= models.CharField(max_length=200)
    image = models.FileField(null=True,blank=True)

# Create your models here.
=======
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
>>>>>>> 4a88c5f00d77a5414f5ca3baefba196a972ce282
