from django import forms
from .models import If

class SearchForm(forms.ModelForm):
	class Meta:
		model = If
		fields = ['journal']
