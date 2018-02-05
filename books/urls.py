from django.urls import path,re_path
from . import views
from django.conf.urls import url

#parent urls add app name before url "/book" for ex
urlpatterns = [
    # path('',views.index,name="index"),
    re_path(r'^$',views.index)
    
]
