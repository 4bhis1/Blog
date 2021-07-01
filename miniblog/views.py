from miniblog.models import Post_the_blog
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout  

# Create your views here.
def home(request):
    posts=Post_the_blog.objects.all()
    return render(request,'miniblog/home.html',{'post':posts})


def about(request):
    return render(request,'miniblog/about.html')

def contact(request):
    return render(request,'miniblog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post_the_blog.objects.all()
        return render(request,'miniblog/dashboard.html',{'post':posts})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method=="POST":
        form=forms.SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!! Now, you are an author.")
            form.save()
    else:
        form=forms.SignUpForm()
    return render(request,'miniblog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=forms.LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)

                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!')
                    # print("------------------> loggedin successfully")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form=forms.LoginForm()
        
        return render(request,'miniblog/login.html',{'form':form})
    else:
        
        return HttpResponseRedirect('/dashboard/')