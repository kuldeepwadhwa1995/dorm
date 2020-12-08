from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.views import View
from .forms import CustomerForm
from django.conf import settings
import random
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from . import forms




# Create your views here.
def customer_view(request):
   context ={} 
   form = CustomerForm(request.POST) # create the object of form 
   if form.is_valid():
      form.save()
      email_value=form.instance.email #get the email value from the form input value
      print(email_value)
      print("create" + smtp_view(request,email_value))# pass the email value as argument before pass the context and concatinate with print statement
   context['form']= form 
   return render(request, "customer_view.html", context)

def smtp_view(request,email_value):
   print("done")
   if request.method=='POST':     
      subject = 'send the mail'
      email_from = settings.EMAIL_HOST_USER
      #html_content = get_template('mail.html').render()
      recipient_list =[email_value]
      otp=random.randrange(1111,9999)
      message=f"your otp is {otp}"
      email =  EmailMultiAlternatives(subject, message, email_from, recipient_list)
      #email.attach_alternative(html_content, "text/html")
      email.send()
      return "done"
   if request.method == 'GET':
      return " GET MEthod"
   
        


