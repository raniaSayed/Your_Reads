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
from users.models import *

class userLogout(View):
    #@login_required
    def get(self,request):
        if request.user.is_authenticated:
            #dict_cont={"user":{"alaa","selvia"},"action":{"reading","wish"},"book":{"b1","b2"}}
            dict_cont={"posts":{"Martina reading lovestory b1","selvia WishReading thetime  b2","mariam WishReading thetime  b3","selvia Reading thetime  b6"}}
            return render(request,'users/home.html',dict_cont)
        else:
           return redirect('register')

    def post(self,request):
        if request.POST.get('submit') == 'logout':
            if request.user.is_authenticated:
                logout(request)
                return redirect('register')
        else:
            return redirect('logout')

class UserFormView(View):
    register_form=UserForm
    login_form=UserFormLogin
    registerForm=register_form(None)
    loginForm=login_form(None)
    template_name='users/registration_form.html'
    #need to display form
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,self.template_name,{'registerform':self.registerForm,'loginForm':self.loginForm,'range': {"b1","b2","b3","b4","b5","b6","b7","b8"}})
        else:
            return redirect('logout')

    # need to submit and save in DB
    def username_present(self,username):
        if User.objects.filter(username=username).exists():
            return True
        return False

   ###########login action
    def login_view(self,request):
        uname =request.POST['username']
        pword =request.POST['password']
        user = authenticate(username=uname, password=pword)
        if user is not None:
            return user
        else:
            return False
###################################################
    def post(self,request):
        if request.POST.get('submit') == 'register':
            form=self.register_form(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                username=form.cleaned_data['username']
                if not self.username_present(username):
                    username=form.cleaned_data['email']
                    password=form.cleaned_data['password']
                    user.set_password(password)
                    user.save()
                    login(request,user)
                    return redirect('logout')

            return render(request,self.template_name,{'registerform':form,'loginForm':self.loginForm,'userExistError':" Username is already in use"})

        elif request.POST.get('submit') == 'login':
            formlogin=self.login_form(request.POST)
            user = self.login_view(request)
            if user:
                login(request,user)
                return redirect('logout')
            else:
                return render(request,self.template_name,{'registerform':self.registerForm,'loginForm':formlogin,'error':" invalid user name or password "})


class UserProfile(View):
    template_name='users/home.html'
    def get(self,request):
         return redirect("logout")

    def post(self,request):
         data=[]
         datadesc=""
         if request.POST.get('submit') == 'Read':
             datadesc="your current read"
             res=ReadNowList.objects.filter(user=request.user.id)
             for item in res:
                 data.append(item.book)

         elif request.POST.get('submit') == 'wish':
             datadesc="your wish  read books"
             res=WishList.objects.filter(user=request.user.id)
             for item in res:
                 data.append(item.book)

         elif request.POST.get('submit') == 'finished':
             datadesc="your finished books"
             res=ReadedList.objects.filter(user=request.user.id)
             for item in res:
                 data.append(item.book)

         elif request.POST.get('submit') == 'rate':
             datadesc="your rated books"
             res=rateList.objects.filter(user=request.user.id)
             for item in res:
                 data.append(item.book)
         dict_cont={"posts":{"Martina reading lovestory b1","selvia WishReading thetime  b2",
         "mariam WishReading thetime  b3","selvia Reading thetime  b6"},'Msg':datadesc,'bookslist':data}
         return render(request,self.template_name,dict_cont)



def hell(request):
    template_name='users/base.html'
    return render(request,template_name)

def hi(request):
    template_name='users/base.html'
    return render(request,template_name)
