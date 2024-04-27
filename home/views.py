from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login as auth_login

# Create your views here.
def index (request):
    context = {
        
    }
    return render(request,'index.html')
    

def about(request):
    return render(request,'about.html')
    
def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def rent(request):
    car_id = request.GET.get('car_id')
    if  request.method =='POST':
        

        return redirect('/payment')
    else:
        return render(request, 'rent.html', {'car_id': car_id})

def register(request):
   if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        
        # Redirect to login page or any other page
        return redirect('/login')
   else:
      return render(request, 'register.html') 
 
def profile(request):
   return render(request, 'profile.html')
 
def logout(request):
    return render(request,'logout.html')
 
 


    
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # Login successful
            auth_login(request, user)  # Use auth_login instead of login
            return redirect('/profile')  # Redirect to profile page after successful login
        else:
            # Invalid login
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
    
def payment(request):
    return render(request, 'payment.html')    