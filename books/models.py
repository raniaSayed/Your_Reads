from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 100)
    # author = models.ForeignKey(Author,on_delete=models.SET_NULL)
    summary = models.TextField()
    link = models.URLField()
    country = models.CharField(max_length= 100)
    published_at = models.DateField()

    def __str__(self):
        return self.title
