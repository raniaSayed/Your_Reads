from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    newAuthor= Authors(author_name="Murakami")
    newAuthor.save()
# Create your views here.
