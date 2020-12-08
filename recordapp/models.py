from django.db import models


# Create your models here.
class Customer(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True,null=True)
    mobile=models.IntegerField()
    city=models.CharField(max_length=30)



    def __str__(self):
        return self.username

    def __str__(self):
        return self.email

    def __str(self):
        return self.mobile

    def __str__(self):
        return self.city
