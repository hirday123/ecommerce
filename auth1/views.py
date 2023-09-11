from django.shortcuts import render
from .forms import SignUpForm,LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def sign_up(req):
    if req.method=="POST":
        fm=SignUpForm(req.POST)
        if fm.is_valid():
            fm.save()
            messages.success(req,'signup succesful')
            fm=SignUpForm()
            return render(req,'auth1/signup.html',{'fm':fm})
    else:
       fm=SignUpForm()
    return render(req,'auth1/signup.html',{'fm':fm})


def log_in(req):
    if req.method=="POST":
        fm=LogInForm(request=req,data=req.POST)
        if fm.is_valid():
            a=fm.cleaned_data['username']
            b=fm.cleaned_data['password']
            user=authenticate(username=a,password=b)
            if user is not None:
                login(req,user)
                #req.session['name']=str(req.user)
                messages.success(req,"LOGIN Successful")
                fm=LogInForm()
                return render(req,'auth1/login.html',{'fm':fm})
    else:
        fm=LogInForm()
    return render(req,'auth1/login.html',{'fm':fm})

def log_out(req):
    logout(req)
    messages.success(req,'logout successfully')
    fm=SignUpForm()
    return render(req,'auth1/signup.html',{'fm':fm})

















'''
def log_in(req):
    if req.method=="POST":
        fm=LogInForm(req.POST)
        if fm.is_valid():
            un=fm.cleaned_data['username']
            pw=fm.cleaned_data['password']
            user=authenticate(username=un,password=pw)
            print(1)
            if user is not None:
              print(1)
              login(req,user)
              messages.success(req,'login succesful')
              return render(req,'auth1/login.html',{'fm':fm})
    else:
       fm=LogInForm()
    return render(req,'auth1/login.html',{'fm':fm})
'''