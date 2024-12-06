from django.contrib.auth.signals import user_logged_in #signal
from django.db.models.signals import pre_save
from django.dispatch import receiver


from django.contrib.auth.models import User #sender

#reciever function
def user_login_success(sender,request,user,**kwargs):
   print("User login success signal")
   print(f"Sender: {sender}")
   print(f"User logged in: {user}")
   print(f"User email: {user.email}")
   print(f"Request path: {request}")
   print(kwargs)
   #write the logic to semd email to the user

user_logged_in.connect(user_login_success,sender=User) #1st method


@receiver(pre_save,sender=User) #2nd method
def pre_save_signal_receiever(sender,**kwargs):
   print("i am pre_save signal")
   print(f"sender: {sender}")
   print(kwargs)