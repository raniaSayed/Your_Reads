from django.urls import path,re_path
from . import views
from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    # url(r'^$', AuthorsList.as_view()),
    # path(author/)
    re_path('(?P<author_id>[0-9]+)/',views.detail_id),
    # re_path('(?P<name>[a-zA-Z]+)/',views.detail_name),
    # re_path('(?P<name>[a-zA-Z]+)/',views.detail_name2),
    # url(author/(?P<pk>[0-9]+)$', views.detail)
]

 # if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
