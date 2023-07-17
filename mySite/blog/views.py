from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse




class Home_View(ListView):
    model = Post
    template_name = 'home_page.html'

def About_Me_View(request):
    return render(request, 'about_me.html',{})

class Blog_details_View(DetailView):
    model = Post
    template_name = 'Post.html'