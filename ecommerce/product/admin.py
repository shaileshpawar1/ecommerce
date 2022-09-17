from django.contrib import admin
from  .models import *
# Register your models here.

admin.site.register(Prodcut_categories) 
admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Order) 
admin.site.register(Cart) 