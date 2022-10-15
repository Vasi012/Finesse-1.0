from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile


class EditProfileForm(UserChangeForm):
    """Edit profile form"""
    email = forms.EmailField(widget=forms.EmailInput
                             (attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput
                                 (attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput
                                (attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput
                               (attrs={'class': 'form-control'}))

    class Meta:
        """Tell the model which fields we edit"""
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email')


class PasswordChangingForm(PasswordChangeForm):
    """Form for change password"""
    old_password = forms.CharField(max_length=100,
                                   widget=forms.PasswordInput
                                   (attrs={'class': 'form-control',
                                           'type': 'password'}))
    new_password1 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                            'type': 'password'}))
    new_password2 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput
                                    (attrs={'class': 'form-control',
                                            'type': 'password'}))

    class Meta:
        """Elements of the form"""
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageForm(forms.ModelForm):
    """Allow new user to edit specific fields"""
    class Meta:
        """Elements of form"""
        model = Profile
        fields = ('bio',
                  'profile_pic',
                  'website_url',
                  'facebook_url',
                  'instagram_url',
                  'twitter_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            }
