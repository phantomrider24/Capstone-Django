from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import User_Register_Form 

# Create your views here.
def user_login(request):
    """user_login is used to render the login.html from the template folder
    """
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    """authenticate_user is a function that asks the user for their username & password and redirect them to the main webpage "blog" if it authenticates
        
        :param str username: The user's username
        :param str password: The user's password
        :param authenticate: If the given credentials are valid, return a User object
        :return: 'True' if user object has been returned to redirect to main page, 'False' redirects back to the same page
    """
    username = request.POST['username']
    password= request.POST['password']
    user = authenticate(username=username, password = password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request,user)
        return HttpResponseRedirect(
            reverse('user_auth:show_page')
        )
    
def show_page(request):
    """The show_page function is to create a direct link to the Blog webapp where if the user is authenticated, the user is redirected to the other site.
    """
    print(request.user.username)
    return HttpResponseRedirect(
        reverse('blog:home_page')
    )

def register_user(request):
    """Register users is a function that allows the user-auth webapp to register users to the admin site if they don't have access to the admin site
       
        :param form: class User_Register_Form is saved to
        :param str username: The new user's username
        :param str password: The new user's password
        :param authenticate: If the given credentials are valid, return a User object
        :return: 'True ' calls for show_page function if user creation is successful, 'False' goes back to the User_Register_Form 
    """
    if request.method == "POST":
        form = User_Register_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password = password) 
            messages.success(request,("Registration completed"))
            return HttpResponseRedirect(
                reverse('user_auth:show_page')
            )
    else:
        form = User_Register_Form()
    return render(request, 'authentication/user_registration.html',{
        'form':form,
    })