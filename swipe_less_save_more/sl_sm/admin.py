# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import userreg,bankdetails,product,discounts

admin.site.register(userreg)

admin.site.register(bankdetails)
admin.site.register(product)
admin.site.register(discounts)
