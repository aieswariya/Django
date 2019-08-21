from django.urls import path
#from myapp.views import *
from . import views
urlpatterns=[
       path('',views.home,name='home'),
       path('result/',views.display,name='display'),
       path('search/',views.search,name='search'),
]
       