from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class IDForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(IDForm, self).__init__(*args, **kwargs)
		self.fields['id_field'].required = False

	id_field = forms.ImageField(label='Upload back side of ID Card ')


class RegForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    iin = forms.CharField(max_length=12)
    birthday = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'dd-MM-yyyy'}))
    password = forms.CharField(widget=PasswordInput())
    password2 = forms.CharField(widget=PasswordInput(), label='Repeat password')
