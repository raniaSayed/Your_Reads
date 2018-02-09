from django.urls import path,re_path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#parent urls add app name before url "/book" for ex
urlpatterns = [
     path('',views.index,name="books"),
     re_path(r'^(?P<id>[0-9]+)/$',views.view),
     re_path(r'^author/(?P<id>[0-9]+)/$',views.get_author_books),
     re_path(r'^rate/(?P<rate_value>[0-5]+)/(?P<book_id>[0-9]+)$',views.rate_book,name="rate_book"),
     re_path(r'^category/(?P<category_id>[0-9]+)$',views.love_category),
     path('read/',views.User_action.as_view(), name='read_book'),
     re_path(r'^search/$',views.search),

]

# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
