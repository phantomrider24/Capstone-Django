from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """Post is a class model for the blog entities

        :param title: str, Title of the blog
        :param author: Author of the blog
        :param body: str, the body of the blog
    """

    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        """string of the class
        """
        return self.title + ' | '+str(self.author)
    
