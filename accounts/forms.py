from django.forms import ModelForm
from .models import Order, User, ClubMember, ClubOrder
from django import forms


class ClubOrderForm(ModelForm):
	class Meta:
		model=ClubOrder
		fields='__all__'


class OrderForm(ModelForm):
	class Meta:
		model=Order
		fields = '__all__'



class RegisterForm(ModelForm):
	class Meta:
		model=User
		fields = '__all__'



class ClubmemberForm(ModelForm):
	class Meta:
		model=ClubMember
		fields = '__all__'