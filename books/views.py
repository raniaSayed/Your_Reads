from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect


from books.models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    # return HttpResponse(book)
    # return JsonResponse({'name': 'Ahmed'})
    # return HttpResponseRedirect("bo")
    return render(request,'index.html',{'books':books})
    # return redirect('/admin',{'name':'ahmed'})

def view(request,id=0):
    #make a middleware for this function to prevent unexistant ids
    # return Book.objects.all().get(id)
    return HttpResponse(id)
