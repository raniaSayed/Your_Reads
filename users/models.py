from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
#
class ReadedList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class ReadNowList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class RatedList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    rate_val = models.IntegerField()

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class rateList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    Choices = (
        (1,  'So Bad'),
        (2,  'Bad'),
        (3,  'Normal'),
        (4,  'High'),
        (5,  'So High'),
      )
    rate = models.IntegerField(default=1, choices=Choices)

class categoryList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey('books.Category',on_delete=models.CASCADE)

# class recommendedList():
#     #user_id=
#     #URecommend=
#     #Book_id=models.ForeignKey(Book,on_delete=models.SET_NULL)
