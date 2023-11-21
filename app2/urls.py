from django.urls import path
from app2.views import *
app_name='anything'

urlpatterns=[
   path('giri/',giri,name='giri'),

]