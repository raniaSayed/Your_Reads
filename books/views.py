from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from books.models import *

# Create your views here.
def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    # return HttpResponse(book)
    # return JsonResponse({'name': 'Ahmed'})
    # return HttpResponseRedirect("bo")

    return render(request,'index.html',{'books':books,'categories':categories,'checked' : range(3),'unchecked':range(2) })
    # return redirect('/admin',{'name':'ahmed'})

def view(request,id):
    #make a middleware for this function to prevent unexistant ids
    return render(request,"single.html",{"book" :Book.objects.get(id=id),'category':""});
    # return HttpResponse(id)

def author(request,id):
    return HttpResponse(Book.objects.get(id=id).author)
