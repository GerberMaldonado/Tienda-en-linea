from django import forms
from orders.models import Client

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'sname': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'dpi': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'number': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),		
		'address': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
		'nit': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		'saldo': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		'limit_credit': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
		}