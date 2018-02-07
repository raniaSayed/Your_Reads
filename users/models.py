from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
class ReadedList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    published_at = models.DateField()


class RatedList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)
    rate_val = models.IntegerField()

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Book',on_delete=models.CASCADE)

# class recommendedList():
#     #user_id=
#     #URecommend=
#     #Book_id=models.ForeignKey(Book,on_delete=models.SET_NULL)
