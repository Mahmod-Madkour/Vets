### account/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import *

####################################################################################################
# Login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={"placeholder": "username",}))
    password = forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={"placeholder": "password"}))

# Register
class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Updtae Profile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'about', 'photo']
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Last Name'})
        self.fields['about'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your About'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Photo'})

# Updtae Password
class UpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
    def __init__(self, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter old password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter new password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm new password'})

####################################################################################################
# Post 
class PostForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "What's on your mind !", "rows": 10}
        )
    )

# Update Post, Comment, Replay 
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body']
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your updated'})

# Comment
class CommentForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!", "rows": 1}
        )
    )

# Replay
class ReplayForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a replay!", "rows": 1}
        )
    )

####################################################################################################
# Question 
class QuestionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your title", "rows": 1}
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter you want here", "rows": 10}
        )
    )

# Answer 
class AnswerForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter you want here", "rows": 10}
        )
    )

# Update Question 
class UpdateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['body', 'status']

    def __init__(self, *args, **kwargs):
        super(UpdateQuestionForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your updated'})
        self.fields['status'].widget.attrs.update({'class': 'form-control', })

####################################################################################################

# Disease 
class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['category', 'body', 'photo']
    def __init__(self, *args, **kwargs):
        super(DiseaseForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Category of Disease'})
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Description of Disease'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'}, required = True)

# Therapy 
class TherapyForm(forms.ModelForm):
    class Meta:
        model = Therapy
        fields = ['body', 'photo']
    def __init__(self, *args, **kwargs):
        super(TherapyForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Description of Therapy'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control'})

    