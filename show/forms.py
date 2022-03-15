from cProfile import label
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': "Choose File for thumbnail & video"
        })
    )
    image = forms.ImageField(
        label='',
        required=False)
    video = forms.FileField(
        label='',
        required=False
    )
    class Meta:
        model = Post
        fields = ['body', 'image', 'video']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Leave a comment...'
        })
    )
    class Meta:
        model = Comment
        fields = ['comment']

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            "class": "form-control"
        }),
        max_length=1000)
    