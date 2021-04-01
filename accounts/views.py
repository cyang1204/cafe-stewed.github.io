from django.shortcuts import render, redirect
from accounts.models import *
# Create your views here.
from django.forms import inlineformset_factory
from django.http import HttpResponse
from .models import *
from .forms import OrderForm, RegisterForm, ClubmemberForm, ClubOrderForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def register(request):
	reg=RegisterForm()
	if request.method=='POST':
		print('Printing POST:', request.POST)
		reg = RegisterForm(request.POST)
		if reg.is_valid():
			reg.save()
			messages.success(request, 'Your details have been saved successfully!')

			return redirect('/', {'reg':reg})
	context={'reg': reg}
	return render(request, 'accounts/register.html', context)

def club_member(request):
	rec=ClubmemberForm()
	if request.method=='POST':
		print('Printing POST:', request.POST)
		rec = ClubmemberForm(request.POST)
		if rec.is_valid():
			rec.save()
			messages.success(request, 'Your details have been saved successfully!')

			return redirect('/', {'rec':rec})
	context={'rec': rec}
	return render(request, 'accounts/club_member.html', context)



def home(request):
	return render(request, 'accounts/dashboard.html')

def menu(request):
	menus=Menu.objects.all()
	return render(request, 'accounts/menu(products).html',{'menus':menus})

def contact(request):
	return render(request, 'accounts/contact.html')




def orders(request):
	orders=Order.objects.all()
	ordersc=ClubOrder.objects.all()
	context={'orders':orders, 'ordersc':ordersc}
	return render(request, 'accounts/orders.html', context)
#render template


def createOrder(request):
	form=OrderForm()
	if request.method=='POST':
		print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your order has been placed successfully!')
			return redirect('/')
	context={'form': form}
	return render(request, 'accounts/create_order.html', context)

def createClubOrder(request):
	formc=ClubOrderForm()
	if request.method=='POST':
		print('Printing POST:', request.POST)
		formc = ClubOrderForm(request.POST)
		if formc.is_valid():
			formc.save()
			messages.success(request, 'Your order has been placed successfully! A discount of 20 percent is added to your bill. Enjoy!')

			return redirect('/')
	context={'formc': formc}
	return render(request, 'accounts/create_club_order.html', context)










def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method=="POST":
		order.delete()
		messages.success(request, 'Your order has been deleted successfully!')
		return redirect('/')
	context = {'item':order}
	return render(request, 'accounts/delete.html', context)





def deleteClubOrder(request, pk):
	orderc = ClubOrder.objects.get(id=pk)
	if request.method=="POST":
		orderc.delete()
		messages.success(request, 'Your order has been deleted successfully!')
		return redirect('/')
	context = {'itemc':orderc}
	return render(request, 'accounts/delete_club.html', context)