from django import forms
from django.contrib.auth.models import User
from .models import User,UserProfile
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class RegistrationForms(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm passwd',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email')
    def clean_password2(self):
        cd =self.cleaned_data
        if cd['password'] != cd ['password2']:
            raise forms.ValidationError('passwords differ')
        return cd['password2']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','birth')
