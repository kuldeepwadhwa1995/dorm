from django.urls import path
from recordapp.views import customer_view
from recordapp.views import smtp_view

urlpatterns = [
    path('',customer_view),
  
]

