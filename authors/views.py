from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView
from .models import Authors



def index(request):
    all_authors = Authors.objects.all()
    html=""
    template_name='authors/index.html'
    name={}
    id={}
    for author in all_authors:
        
        url = '/author/' + str(author.id) + '/'
        html+= '<a href=" '+ url +'  "> '+ author.author_name +' </a> <br> '
    return render(request,template_name,{"name":name,"id":id})

    #return HttpResponse(html)

def detail_id(request, author_id):
        try:
            author=Authors.objects.get(pk=author_id)
            return HttpResponse("<h2> Details for Authors:" + author.author_name+"   "+author.author_nationality + "</h2>")
        except:
            return HttpResponse("not exist")


def detail_name2(request, name):
    author=Authors.objects.filter(author_name__iexact=name)
    if author:
        html=""
        for a in author:
             html+= '<h2>'+ a.author_nationality +' </h2> <br> '
        return HttpResponse(html)

    else:
        return HttpResponse("user isn`t exist ")

def detail_name(request, name):
    author=Authors.objects.filter(author_name__iexact=name)
    if author:
        html=""
        for a in author:
            url = '/author/' + str(a.author_name) + '/'
            html+= '<a href=" '+ url +'  "> '+ a.author_name +' </a> <br> '
             # html+= '<h2>'+ a.author_nationality +' </h2> <br> '
        return HttpResponse(html)

    else:
        return HttpResponse("user isn`t exist ")
