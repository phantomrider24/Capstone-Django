from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse




class Home_View(ListView):
    """This class is a form from the django generic forms which Render some list of objects

        :param model: is the allies that saves the Posts  
        :param template_name: loads the template which is gonna be used for this function  
    """
    model = Post
    template_name = 'home_page.html'

def About_Me_View(request):
    """About_Me_View function is a render function to my personal page with information about the developer
    """
    return render(request, 'about_me.html',{})

class Blog_details_View(DetailView):
    """This class represent the blog details and posts the details to the post.html file

        :param model: is the allies that saves the Posts  
        :param template_name: loads the template which is gonna be used for this function 
    """
    model = Post
    template_name = 'Post.html'