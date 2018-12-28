# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import product
from .models import discounts
from .models import userreg
from .models import bankdetails

# Create your views here.
def index(request):
	return HttpResponse("Hello world")

def display_products(request):
	productlist=product.objects.all()
	discountslist=discounts.objects.all()
	'''for k in productlist:
		print(k.pname)
	for j in discountslist:
		print(j.bankname)
		print(j.discountPercent)
		print(j.p_id)'''
	
	print("products discounts list")	
	list1=[]	
	for k in productlist:
		for j in discountslist:
			print("*")
			print(str(k.pname))
			print(str(j.p_id))
			
			if(str(k.pname)==str(j.p_id)):
					

				list1.append([k.pname,j.bankname,j.discountPercent])
	print(list1)


	'''userbanklist=bankdetails.objects.get(user_id=request.session['usr'])
	for k in userbanklist:
		print(k.bank_name)'''

	userbanklist=bankdetails.objects.all()
	print("session")
    
	
	print(type(request.session['user_id']))

	print("user account details")

	for k in userbanklist:
		print(type(k.user_id))
		if(str(k.user_id)==str(request.session['user_id'])):
			print(k.bank_name)
			
			print(k.account_number)
			print(k.user_id)

	print("user offers according to banks")		
			
	list2=[]

	for k in list1:
		for j in userbanklist:
			if(str(j.user_id)==	str(request.session['user_id'])):
				if(str(k[1])==str(j.bank_name)):
					print(k)
					list2.append(k)	

	'''list1=[]
	smax=0
	tmax=0
	for k in list2:
		if(str(k[0])=="soap"):
			if(smax<int(k[2])):
				smax=int(k[2])

			
		if(str(k[0])=="television"):
			if(tmax<int(k[2])):
				tmax=int(k[2])
	k= str(smax)

	print("soap--->"+k)
	print("telivision--->"+tmax)'''
			






	return render(request, 'sl_sm/display_products.html',{'output':list1,'output1':list2})



def login(request):
	return render(request,'sl_sm/login.html')    

def taking_id(request):
	if request.method == 'POST':
		mail_id=request.POST['email']
		list1=userreg.objects.all()
		for k in list1:
			if(k.email==mail_id):
				request.session['user_id']=k.user_id
		return display_products(request)			





		#return HttpResponse(mail_id)


	

    