from django import forms

from .models import Instagram

class InstagramForm(forms.ModelForm):
	class meta:
		model = Instagram
		fields = [
			'first_name',
			'last_name',
			'username',
		]