from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Comment form for post / blog"""
    class Meta:
        """Meta model and body for form"""
        model = Comment
        fields = ('body',)
