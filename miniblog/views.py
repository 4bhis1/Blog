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

def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=forms.PostForm(request.POST)
            if form.is_valid:
                form.save()
                form=forms.PostForm()
                return HttpResponseRedirect('/dashboard/')
        else:
            form=forms.PostForm()
        return render(request,'miniblog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def update(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post_the_blog.objects.get(pk=id)
            form=forms.PostForm(request.POST,instance=pi)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=Post_the_blog.objects.get(pk=id)
            form=forms.PostForm(instance=pi)
        return render(request,'miniblog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post_the_blog.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def about(request):
    return render(request,'miniblog/about.html')

def contact(request):
    return render(request,'miniblog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        # if request.method=="POST":
        posts=Post_the_blog.objects.all()
        user=request.user
        full_name=user.get_full_name()

        return render(request,'miniblog/dashboard.html',{'post':posts,'fullname':full_name})
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