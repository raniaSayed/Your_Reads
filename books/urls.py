from django.urls import path,re_path
from . import views
from django.conf.urls import url

#parent urls add app name before url "/book" for ex
urlpatterns = [
     path('',views.index,name="index"),
     re_path(r'^(?P<id>[0-9]+)/$',views.view),
     re_path(r'^author/(?P<id>[0-9]+)/$',views.get_author_books),

]



# if the DEBUG is on in settings, then append the urlpatterns as below
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
