from django import forms

from .models import Insstagram

class InstagramForm(forms.ModelForm):
	class meta:
		model = Instagram
		fields = [
			'nama_belakang',
			'nama_depan',
			'username',
		]