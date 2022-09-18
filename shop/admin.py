from django.contrib import admin

from.models import Order, OrderUpdate, product,Contact

# Register your models here.

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
