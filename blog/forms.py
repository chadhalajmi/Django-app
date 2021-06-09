from django.forms.models import ModelForm
from blog.views import post
from django import forms

from .models import Comment,post

class postForm(ModelForm):
    class Meta :
        model = post
        fields = "__all__"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
    