from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Authors


def index(request):
    # newAuthor= Authors(author_name="Murakami",nationality="japanese")
    # newAuthor.save()
    all_authors = Authors.objects.all()
    html=""
    for author in all_authors:
        url = '/author/' + str(author.id) + '/'
        html+= '<a href=" '+ url +'  "> '+ author.author_name +' </a> <br> '
    return HttpResponse(html)

def detail(request, author_id):
    # all_authors = Authors.objects.all()
    # html=""
    # for author in all_authors:
    #     url = '/author/'
    #     html+= '<a href=" '+ url +'  "> '+ author.author_nationa +' </a> <br> '
    # return HttpResponse(html)
    try:
        author=Authors.objects.get(pk=author_id)
        return HttpResponse("<h2> Details for Authors:" + author.author_name+"   "+author.author_nationality + "</h2>")
    except:
        return HttpResponse("not exist")





# class AuthorsList(ListView):
#     model = Authors
#
# class AuthorsView(DetailView):
#     model = Authors
