from django import forms
from .models import *
payment= [
    ('Employee','Employee'),
    ('Other','Other'),
]

class Employee_form(forms.ModelForm):
      name=forms.CharField(widget=forms.TextInput(attrs={'class':'from-control','placeholder':'Enter Name'}),required=True,max_length=100)
      account_number=forms.CharField(widget=forms.TextInput(attrs={'class':'from-control','placeholder':'Enter Account_number'}),required=True,max_length=10)
      ifsc=forms.CharField(widget=forms.TextInput(attrs={'class':'from-control','placeholder':'Enter IFSC'}),required=True,max_length=10)
      payment_type= forms.CharField(label='payment_type', widget=forms.Select(choices=payment))
      
      class Meta:
           model= Employee
           fields=('name','account_number','ifsc','payment_type')
           
      def clean_account_number(self):
         acc=self.cleaned_data['account_number']
         try:
            match=Employee.objects.get(account_number=acc)
         except:
           return self.cleaned_data['account_number']
         raise forms.ValidationError("exist account_ number")
      