from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import TextInput, PasswordInput

from .models import Record

INPUT_CLASSES = 'form-control form-control-lg'


# - register/Create a user

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

	username = forms.CharField(widget= TextInput(attrs={
		'placeholder': 'Your username',
		'class': INPUT_CLASSES
		}))
	password1 = forms.CharField(widget= PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': INPUT_CLASSES
		}))
	password2 = forms.CharField(widget= PasswordInput(attrs={
		'placeholder': 'Repeat password',
		'class': INPUT_CLASSES
		}))



# - Login a user

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget = TextInput(attrs={
		'placeholder': 'Your username',
		'class': INPUT_CLASSES
		}))
	password = forms.CharField(widget = PasswordInput(attrs={
		'placeholder': 'Your password',
		'class': INPUT_CLASSES
		}))


# - Create/Add a new record

class CreateRecordForm(forms.ModelForm):

	class Meta:

		model = Record
		fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
		widgets = {
				'first_name': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'last_name': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'email': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'phone': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'address': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'city': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'province': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'country': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					})
			}
		



# - Update a new record

class UpdateRecordForm(forms.ModelForm):

	class Meta:

		model = Record
		fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
		widgets = {
				'first_name': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'last_name': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'email': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'phone': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'address': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'city': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'province': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					}),
				'country': forms.TextInput(attrs={
					'class': INPUT_CLASSES
					})
			}


