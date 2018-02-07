from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Authors


def index(request):
    # newAuthor= Authors(author_name="Murakami",nationality="japanese")
    # newAuthor.save()
    all_authors = Authors.objects.all()
    template = loader.get_template('authors/index.html')
    context= {
    'all_authors': all_authors,
    }
    return HttpResponse('')

def detail(request, author_id):
    return HttpResponse("<h2> Details for author:" + str(author_id) + "</h2>")


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
#             author=Authors.objects.get(pk=author_id)
#             return HttpResponse("<h2> Details for Authors:" + author.author_name+"   "+author.author_nationality + "</h2>")
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
