from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm,UserFormLogin
from django.views.generic import ListView, DetailView
from django.template import loader
from django.http import Http404
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

class userLogout(View):
    #@login_required
    def get(self,request):
        if request.user.is_authenticated:
            return render(request,'users/base.html')
        else:
           return redirect('register')

    def post(self,request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('register')


class UserFormView(View):
    # def get(self,request):
    #     return HttpResponse("ddkdkd")

    register_form=UserForm
    login_form=UserFormLogin
    registerForm=register_form(None)
    loginForm=login_form(None)
    template_name='users/registration_form.html'
    #need to display form
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,self.template_name,{'registerform':self.registerForm,'loginForm':self.loginForm})
        else:
            return redirect('logout')

#     # need to submit and save in DB
#     def username_present(self,username):
#         if User.objects.filter(username=username).exists():
#             return True
#         return False
#
#    ###########login action
#     def login_view(self,request):
#         uname =request.POST['username']
#         pword =request.POST['password']
#         user = authenticate(username=uname, password=pword)
#         if user is not None:
#             return user
#         else:
#             return False
# ###################################################
#     def post(self,request):
#         if request.POST.get('submit') == 'register':
#             form=self.register_form(request.POST)
#             if form.is_valid():
#                 user=form.save(commit=False)
#                 username=form.cleaned_data['username']
#                 if not self.username_present(username):
#                     username=form.cleaned_data['email']
#                     password=form.cleaned_data['password']
#                     user.set_password(password)
#                     user.save()
#                     login(request,user)
#                     return redirect('logout')
#
#             return render(request,self.template_name,{'registerform':form,'loginForm':self.loginForm,'userExistError':" Username is already in use"})
#
#         elif request.POST.get('submit') == 'login':
#             formlogin=self.login_form(request.POST)
#             user = self.login_view(request)
#             if user:
#                 login(request,user)
#                 return redirect('logout')
#             else:
#                 return render(request,self.template_name,{'registerform':self.registerForm,'loginForm':formlogin,'error':" invalid user name or password "})
#
# def hell(request):
#     template_name='users/base.html'
#     return render(request,template_name)
#
# def hi(request):
#     template_name='users/base.html'
#     return render(request,template_name)
