from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Authors
from books.models import Book

def index(request):
    all_authors = Authors.objects.all()
    template = loader.get_template('authors/index.html')
    context= { #this is the info my template need
    'all_authors': all_authors,
    }
    return render(request, 'authors/index.html',context)
    # return HttpResponse(template.render(context, request))

def detail_id(request, author_id):
    author=Authors.objects.get(pk=author_id)
    books=Book.objects.filter(author=author_id)
    template = loader.get_template('authors/detail.html')
    context= { #this is the info my template need
    'author': author,
    'books': books,
    }
    return render(request, 'authors/detail.html',context)

def detail_name(request, name):
     authors=Authors.objects.filter(author_name__iexact=name)
     template = loader.get_template('authors/detailName.html')
     context= { #this is the info my template need
     'authors': authors,
     }
     return render(request, 'authors/detailName.html',context)

# def detail_name_id(request,name, author_id):
#     author=Authors.objects.get(pk=author_id)
#     books=Book.objects.filter(author=author_id)
#     template = loader.get_template('authors/detail.html')
#     context= { #this is the info my template need
#     'author': author,
#     'books': books,
#     }
#     return render(request, 'authors/detail.html',context)


# def get_author_books(request,a_id):
#     books=Book.objects.filter(author=a_id)
#     author=Authors.objects.get(pk=a_id)
#     template = loader.get_template('authors/book.html')
#     context={ 'books': books, 'author': author}
#     return render(request,'authors/book.html',context)
    # return HttpResponse("hi")

        # return HttpResponse(template.render(context, request))

        #     return HttpResponse("<h2> Details for Authors:" + author.author_name+"   "+author.author_nationality + "  "+author.born_at
        # +" "+author.died_at+" "+author.books+" "+author.image+" "+author.bio+"</h2>")
        # except:
        #     return HttpResponse("not exist")

# def detail(request, author_id):
#     return HttpResponse("<h2> Details for author:" + str(author_id) + "</h2>")
#

# def delete(request):
#         all_authors = Authors.objects.all()
#         all_authors.delete()
#         return HttpResponse("hi")


# def index(request):
#     # newAuthor= Authors(author_name="Murakami",nationality="japanese")
#     # newAuthor.save()
#     all_authors = Authors.objects.all()
#     html=""
#     for author in all_authors:
#         url = '/author/' + str(author.id) + '/'
#         html+= '<a href=" '+ url +'  "> '+ author.author_name +' </a> <br> '
#     return HttpResponse(html)
#
# def detail_id(request, author_id):
#         try:
#
#             author=Authors.objects.get(pk=author_id)
#             return HttpResponse("<h2> Details for Authors:" + author.author_name+"   "+author.author_nationality+ "  "+author.image+"</h2>")
#         #     return HttpResponse("<h2> Details for Authors:" + author.author_name+"   "+author.author_nationality + "  "+author.born_at
#         # +" "+author.died_at+" "+author.books+" "+author.image+" "+author.bio+"</h2>")
#         except:
#             return HttpResponse("not exist")
#
#
# def detail_name(request, name):
#     author=Authors.objects.filter(author_name__iexact=name)
#     if author:
#         html=""
#         for a in author:
#              html+= '<h2>'+ a.author_nationality +' </h2> <br> '
#         return HttpResponse(html)
#
#     else:
#         return HttpResponse("user isn`t exist ")
#
# def detail_name2(request, name):
#     author=Authors.objects.filter(author_name__iexact=name)
#     if author:
#         html=""
#         for a in author:
#             url = '/author/' + str(a.author_name) + '/'
#             html+= '<a href=" '+ url +'  "> '+ a.author_name +' </a> <br> '
#              # html+= '<h2>'+ a.author_nationality +' </h2> <br> '
#         return HttpResponse(html)
#
#     else:
#         return HttpResponse("user isn`t exist ")
