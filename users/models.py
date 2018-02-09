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

# class recommendedList():
#     #user_id=
#     #URecommend=
#     #Book_id=models.ForeignKey(Book,on_delete=models.SET_NULL)
