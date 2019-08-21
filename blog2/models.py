from django.db import models


class Employee(models.Model):
      name=models.CharField(max_length=100)
      account_number=models.CharField(max_length=100)
      ifsc=models.CharField(max_length=100)
      payment_type=models.CharField(max_length=100,default="other")
      
      def __str__(self):
           return self.name