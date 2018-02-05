from django.urls import path
from . import views

urlpatterns = [
        path('', views.UserFormView.as_view(), name='register'),
        path('home/', views.userLogout.as_view(), name='logout'),
        #path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
        path('users/', views.hell, name='user'),
        path('hello/', views.hi, name='hh'),
]
