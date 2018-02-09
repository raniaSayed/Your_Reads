from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from books.models import *
from authors.models import *
from users.models import *
from django.db.models import Avg
from math import ceil
<<<<<<< HEAD
from django.views.generic import View
=======
import requests
from django.views.decorators.csrf import csrf_exempt

>>>>>>> 1b50527ebd556c1bcc0fcadc1a8ca224d1c1f746

# Create your views here.
def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    favourite_categories =  categoryList.objects.filter(user_id= request.user.id).values_list('category_id',flat=True)
    return render(request,'index.html',
    {'books':books,'categories':categories,
    'favourites':favourite_categories})


def view(request,id):
    #make a middleware for this function to prevent unexistant ids
    book = Book.objects.get(id=id)
    summary = book.summary
    rate = rateList.objects.filter(book_id = id ).aggregate(Avg('rate'))["rate__avg"]
    if(rate is None):
        rate = 0

    categories = book.categories.all()
    unchecked = ceil(5-int(rate))

    return render(request,"single.html",
    {"book":book,"summary":summary,
    'categories':categories,
    'checked' : rate,'unchecked':unchecked});

@csrf_exempt
def search(request):
    #create SearchForm Class

    book_name = request.POST['search_word']
    books = Book.objects.filter(title__icontains= book_name)
    return render(request,'index.html',
    {'books':books})

# return books of specific author
def get_author_books(request,id):
    return HttpResponse(Book.objects.filter(author=id))


#insert new rate to specific book
def rate_book(request,rate_value,book_id):
    rate = rateList(user_id= request.user.id,book_id = book_id,rate = rate_value )
    rate.save()
    return JsonResponse(1,safe=False)

def love_category(request,category_id):
    category = categoryList(user_id= request.user.id,category_id=category_id)
    category.save()
    return JsonResponse(1,safe=False)



class User_action(View):

    def get(rself,request):
        return redirect('books')

    def post(self,request):
        if request.POST.get('submit') == 'Read':
            user_read=ReadNowList(user_id= request.user.id,book_id = request.session.get('book_id'))
            user_read.save()
        elif request.POST.get('submit') == 'wish':
                user_read=WishList(user_id= request.user.id,book_id = request.session.get('book_id'))
                user_read.save()
        elif request.POST.get('submit') == 'finished':
                user_read=ReadedList(user_id= request.user.id,book_id = request.session.get('book_id'))
                user_read.save()
        return redirect('books')
