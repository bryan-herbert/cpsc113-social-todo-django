from django import forms
        
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(attrs={'placeholder': 'first & last name'}))
    email = forms.EmailField(max_length=50, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    passwordConfirmation = forms.CharField(max_length=50, label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label='E-mail', widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    password = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    
class newTaskForm(forms.Form):
    taskTitle = forms.CharField(max_length=500, label='Task Info', widget=forms.TextInput(attrs={'placeholder': 'Task Title'}))
    taskDescription = forms.CharField(max_length=5000, label='Task Description', widget=forms.TextInput(attrs={'placeholder': 'description'}))
    collaborator1 = forms.CharField(max_length=100, required=False, label='collaborators', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    collaborator2 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    collaborator3 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))