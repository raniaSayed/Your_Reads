from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect


from books.models import Book

# Create your views here.
def index(request):
    book = Book.objects.all()
    # return HttpResponse(book)
    # return JsonResponse({'name': 'Ahmed'})
    # return HttpResponseRedirect("bo")
    return render(request,'index.html',{'name':'ahmed'})
    # return redirect('/admin',{'name':'ahmed'})
