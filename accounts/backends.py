# customize sign in
from django.contrib.auth.backends import BaseBackend
from .models import Account

class MyBackEnd(BaseBackend):
    def authenticate(self,request,email=None,password=None,**kwargs):
        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return None
        
        if user.check_password(password):
            return user
        
    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None
        
# if your using the above code for your custom login then use the bellow code in navbar.html 
# {% if request.user.is_authenticated %}
# <small class="title text-muted">Welcome! {{ request.user.first_name }}</small>