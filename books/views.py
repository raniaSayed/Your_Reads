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

# Create your views here.
def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    # return HttpResponse(book)
    # return JsonResponse({'name': 'Ahmed'})
    # return HttpResponseRedirect("bo")
    return render(request,'index.html',{'books':books,'categories':categories,'checked' : range(3),'unchecked':range(2) })
    # return redirect('/admin',{'name':'ahmed'})

################ except for get book category ###################
def view(request,id):
    #make a middleware for this function to prevent unexistant ids
    rate = rateList.objects.filter(book_id = id ).aggregate(Avg('rate'))["rate__avg"]
    # book_categories = Book.objects.filter(id = id).categories
    return render(request,"single.html",{"book" :Book.objects.get(id=id),'category':"",'checked' : rate,'unchecked':ceil(5-int(rate))});
    # return JsonResponse({"rate":book_categories})

# return books of specific author
def get_author_books(request,id):
    return HttpResponse(Book.objects.filter(author=id))


#insert new rate to specific book
def rate_book(request,rate_value,book_id):
    rate = rateList(user_id= request.user.id,book_id = book_id,rate = rate_value )
    rate.save()
    return JsonResponse(1)
#categories

# def get_categories(request,categ_id):
#     categoris = Category.objects.all()
#     template = loader.get_template('books/categ.html')
#     context= { #this is the info my template need
#     'categoris': categoris,
#     }
#     return render(request, 'books/categ.html',context)
