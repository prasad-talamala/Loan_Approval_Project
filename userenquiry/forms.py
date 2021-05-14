from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                help_text="Required. please enter your first name.")
    lastname = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
                               help_text="Required. please enter your last name.")
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             help_text="Required. please enter your personal email id.")

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
