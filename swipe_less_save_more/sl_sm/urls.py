from django.conf.urls import url
from . import views
app_name = 'sl_sm'

urlpatterns = [

    url('display_products', views.display_products, name='display_products'),
 
 	url('login', views.login, name='login'),
 	url('taking_id', views.taking_id, name='taking_id'),
 ]
