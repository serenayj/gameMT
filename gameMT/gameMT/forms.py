from django import forms
from django.forms import ModelForm
from sampleapp.models import User,Items


class UserForm(ModelForm):

	class Meta:
		model = User
		fields=("username","userid","password","email")


class LoginForm(ModelForm):
	class Meta:
		model = User
		fields=("userid","password")


"""class ItemsForm(ModelForm):
	class Meta:
		model = Items
		fields = ("itemsid","itemname","comments","ratings","decision","userid_id","price")
		"""

		
			
