from django import forms

class RegisterForm(forms.Form):
    #Keep in mind character length if tests are failing
    name = forms.CharField(label='First & Last Name', max_length=30)
    email = forms.CharField(label='E-mail', max_length=30)
    password = forms.CharField(label='Password', max_length=30)
    passwordConfirmation = forms.CharField(label='Password Confirmation', max_length=30)
    f.cleaned_data

# class LoginForm(forms.Form):
#     email = 