from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)

    
class AddUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password_1 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Password")
    password_2 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Re-enter password")
    name = forms.CharField(max_length=64)
    surname = forms.CharField(max_length=64)
    email = forms.EmailField(max_length=64)


class ResetPasswordForm(forms.Form):
    password_1 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Password")
    password_2 = forms.CharField(widget=forms.PasswordInput, min_length=5, label="Re-enter password")
