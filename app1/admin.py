from django.contrib import admin
from .models import *

admin.site.register(Product)  # Fixed model name
admin.site.register(Contact)  # Fixed model name
admin.site.register(Order)
admin.site.register(CartItem)
