from django.contrib import admin
from .models import Service, ServicePrice, Car, ClientCar, Client, Order, OrderLine

# Register your models here.
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(Car)
admin.site.register(ClientCar)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderLine)
