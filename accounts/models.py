from django.db import models

# Create your models here.


class ClubMember(models.Model):
	name=models.CharField(max_length=200, null=True)
	emailid=models.CharField(max_length=200, null=True)
	password=models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name




class User(models.Model):
	name=models.CharField(max_length=200, null=True)
	emailid=models.CharField(max_length=200, null=True)
	password=models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name


class Menu(models.Model):
	image = models.ImageField(upload_to="gallery", default='C:/Users/Ivanka/Desktop/dbmsproject/static/images/dish/picn.jpeg')
	dishname=models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description=models.CharField(max_length=400, null=True)


	def __str__(self):
		return self.dishname


class ClubOrder(models.Model):
	QUANTITY =(
		('Large', 'Large'),
		('Medium', 'Medium'),
		('Small', 'Small'),
		)
	
	Club_Member=models.ForeignKey(ClubMember, null=True, on_delete=models.SET_NULL)
	menu=models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
	quantity=models.CharField(max_length=100, null=True, choices=QUANTITY)
	price = models.FloatField(null=True)
	Table_No=models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.menu.dishname


class Order(models.Model):
	QUANTITY =(
		('Large', 'Large'),
		('Medium', 'Medium'),
		('Small', 'Small'),
		)
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	menu=models.ForeignKey(Menu, null=True, on_delete=models.SET_NULL)
	quantity=models.CharField(max_length=100, null=True, choices=QUANTITY)
	price = models.FloatField(null=True)
	Table_No=models.CharField(max_length=10, null=True)

	def __str__(self):
		return self.menu.dishname
