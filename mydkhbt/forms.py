from django import forms
from .models import Post
from django.db import models
from django.conf import settings


class UpdkhbtForm(forms.Form):
    title = forms.CharField(label='Nhan đề', max_length=200)
    body = forms.CharField(label='Bài viết')

    def save(self):
        Post.objects.create(title=self.cleaned_data['title'], body=self.cleaned_data['body'])
