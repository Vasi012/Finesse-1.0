from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Comment form for post / blog"""
    class Meta:
        """Meta model and body for form"""
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """Allow users to have post a blog post"""
    class Meta:
        """Allow user to have access just to certain fields"""
        model = Post
        fields = ('title',
                  'featured_image',
                  'content')

        widgets = {
            'title': forms.TextInput(attrs={'class':
                                            'form-control',
                                            'placeholder':
                                            'This is the blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                             'This is the message space,'
                                             ' please be respectfully!'}),
        }


class UpdatePostForm(forms.ModelForm):
    """Allow user to update their post"""
    class Meta:
        """Allow user to have access just to certain fields"""
        model = Post
        fields = ('title',
                  'featured_image',
                  'content')

        widgets = {
            'title': forms.TextInput(attrs={'class':
                                            'form-control',
                                            'placeholder':
                                            'This is the blog title'}),
            'content': forms.Textarea(attrs={'class':
                                             'form-control',
                                             'placeholder':
                                             'This is the message space,'
                                             'please be respectfully!'}),
        }
