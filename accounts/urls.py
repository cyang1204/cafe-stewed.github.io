from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name="home"),
    path('menu/',views.menu, name="menu"),
    path('contact/',views.contact, name="contact"),
    path('orders/',views.orders, name="orders"),
	#path('update_item/',views.updateItem, name="update_item"),
    path('register/',views.register, name="register"),
    #path('login/',views.login, name="login"),
    path('club_member/',views.club_member, name="club_member"),
    path('create_club_order/',views.createClubOrder, name="create_club_order"),
    path('create_order/',views.createOrder, name="create_order"),
    path('delete_order/<str:pk>/',views.deleteOrder, name="delete_order"),
    path('delete_club/<str:pk>/',views.deleteClubOrder, name="delete_club"),


]