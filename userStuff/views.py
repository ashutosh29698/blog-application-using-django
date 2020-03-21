from django.shortcuts import render,redirect
from .forms import UserCreateForm, LoginForm
import random as r
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    # if the UserCreateForm is submitted using POST...
    
    if(request.method == 'POST'):
        form = UserCreateForm(request.POST)
        if(form.is_valid()):
            form.save()
            # The user is added successfully!
            messages.add_message(request,messages.SUCCESS, 'Account Created Successfully!')

    else:

        # if user is already logged in
        if(request.user.is_authenticated):
            return redirect('home')

        # if it is a GET request
        form = UserCreateForm()

        # here I tried to create random number each time captcha is loaded
        num1 = r.randint(0,9)
        num2 = r.randint(0,9)

        form.initial['num1'] = num1
        form.initial['num2'] = num2

    # no matter what the request is, log in form needs to be rendered
    loginform = LoginForm()

    return render(request,"index.html",{'form': form, 'loginform': loginform})


@require_POST
def login(request):
    # This function can be accessed only through POST request
    loginform = LoginForm(request,data=request.POST)

    if(loginform.is_valid()):
        # if all the details entered are valid
        username,password = loginform.cleaned_data['username'], loginform.cleaned_data['password']

        # check if such user exist or not
        user = authenticate(username=username,password=password)
        
        if(user):
            # if it exists then login else throw error of not found
            auth_login(request,user)
            # after logging in successfully, redirect to home page
            return redirect('home')
        
    # The following code is used just to be consistent with UserCreateForm which is
    # on the same page.
    form = UserCreateForm()
    num1 = r.randint(0,9)
    num2 = r.randint(0,9)
    
    form.initial['num1'] = num1
    form.initial['num2'] = num2
    
    return render(request,"index.html",{'loginform': loginform, 'form': form})

    