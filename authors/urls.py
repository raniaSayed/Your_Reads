from django.urls import path,re_path
from . import views
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.index,"authors","register"),name="authors"),
    re_path('(?P<name>[a-zA-Z]+)/',login_required(views.detail_name,"auth","register"),name="auth"),
    re_path('(?P<name>[a-zA-Z]+)/(?P<author_id>[0-9]+)/',login_required(views.detail_id,"auth2","register"),name="auth2"),
    re_path('(?P<author_id>[0-9]+)/',login_required(views.detail_id,"author_id","register"),name="author_id"),
    # re_path('(?P<a_id>[0-9]+)/',views.get_author_books),

    # re_path('(?P<name>[a-zA-Z]+)/',login_required(views.detail_name,"author_name","register"),name="author_name"),
    # re_path('(?P<name>[a-zA-Z]+)/',views.detail_name2),
    # url(author/(?P<pk>[0-9]+)$', views.detail)
]

 # if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
