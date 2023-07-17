from django.urls import path
from .views import Home_View, Blog_details_View, About_Me_View

app_name = 'blog'

urlpatterns = [
    path('', Home_View.as_view(), name = 'home_page'),
    path('<int:pk>', Blog_details_View.as_view(), name ='blog-detail'),
    path('about_me',About_Me_View,name='about_me'),
]
