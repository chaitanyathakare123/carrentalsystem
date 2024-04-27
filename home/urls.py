from django.contrib import admin
from django.urls import path
from home import views
from .views import login_view
from .views import payment
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'), 
    path("rent", views.rent, name='rent') ,
    path("register", views.register, name='register'),
    path("profile", views.profile, name='profile'),  
    path("login", login_view, name='login'),
    path("logout", views.logout, name='logout'),
    path('payment/', payment, name='payment'),

]

