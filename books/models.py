from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return  self.name

class Book(models.Model):
    title = models.CharField(max_length= 100)
    author = models.ForeignKey('authors.Authors',null=True,on_delete=models.SET_NULL)
    # category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    summary = models.TextField()
    link = models.URLField()
    country = models.CharField(max_length= 100)
    published_at = models.DateField()
    image = models.FileField(null=True,blank=True)
    #many to many relationship to categories
    categories = models.ManyToManyField(Category)


    # Choices = (
    #     (1,  'So Bad'),
    #     (2,  'Bad'),
    #     (3,  'Normal'),
    #     (4,  'High'),
    #     (5,  'So High'),
    #   )
    # rate = models.IntegerField(default=3, choices=Choices)

    def __str__(self):
        return self.title
