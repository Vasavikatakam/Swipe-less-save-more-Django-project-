# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models







# Create your models here.



class userreg(models.Model):
	user_id=models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=12,unique=True)
	user_pn=models.CharField(max_length=10)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	def __str__(self):
		return str(self.user_id)


class bankdetails(models.Model):
	
	account_number=models.CharField(max_length=50)
	bank_name=models.CharField(max_length=50)
	user_id=models.ForeignKey(userreg,on_delete=models.CASCADE)
	def  __str__(self):
		return self.bank_name


class product(models.Model):
    p_id=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=30)
    def  __str__(self):
		return self.pname
class discounts(models.Model):
	bankname=models.CharField(max_length=15)
	discountPercent=models.IntegerField()
	p_id=models.ForeignKey(product,on_delete=models.CASCADE)
	def __str__(self):
		return (str(self.p_id)+self.bankname+str(self.discountPercent))

		







