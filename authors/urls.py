from django.urls import path,re_path
from . import views
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('',views.index),
    # url(r'^$', AuthorsList.as_view()),
    # path(author/)
    re_path('(?P<author_id>[0-9]+)/',views.detail_id),
    re_path('(?P<name>[a-zA-Z]+)/',views.detail_name),
    # re_path('(?P<name>[a-zA-Z]+)/',views.detail_name2),
    # url(author/(?P<pk>[0-9]+)$', views.detail)
]
