from django.urls import path,re_path
from . import views

#parent urls add app name before url "/book" for ex
urlpatterns = [
    # path('',views.index,name="index"),
    re_path(r'^$',views.index),
    # path('view/<id:integer>',views.view)
    re_path(r'^view/(?P<id>[0-9]+)/$',views.view)
]
