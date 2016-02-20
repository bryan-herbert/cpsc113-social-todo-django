from django import forms
        
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(attrs={'placeholder': 'first & last name'}))
    email = forms.EmailField(max_length=50, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    passwordConfirmation = forms.CharField(max_length=50, label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))