from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Account
from django.contrib.auth.decorators import login_required
# Create your views here.

def registration_form(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account created successfully")
            return redirect('home')
        else:
            for field,errors in form.errors.items():
                for error in errors:
                    messages.error(request,f"{field.capitalize()}:{error}")
            return render(request,'register_form.html',{'form_data':form})
    return render(request, 'register_form.html', {'form_data': form})

# def login_form(request):
#     if request.method=="POST":
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request,user)
#                 redirect('home')
#             else:
#                 form = UserLoginForm()
#                 messages.error(request,'Account not found or incorrect credentials', {'form_data':form})
#     else:
#         form = UserLoginForm()
#     return render(request,'login.html',{'form_data': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Account.objects.get(email = email)
        if user.check_password(password):
            auth_login(request,user)
            # auth_login(request,user, backend='accounts.backends.MyBackend')
            messages.success(request,f'Welcome {email} You have logged in Successfully.')
            return redirect('home')
        else:
            messages.error(request,"Invalid login credentials")
    return render(request,'login.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request,f'You have logged out')
    return redirect('home')