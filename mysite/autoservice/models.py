from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField('Name', max_length=200, help_text='Enter name of the service (ex. oil change)')

    def __str__(self):
        return self.name


class ServicePrice(models.Model):
    car_id = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    service_id = models.ForeignKey('Service', verbose_name='Service', on_delete=models.SET_NULL, null=True)
    price = models.FloatField('Price')

    def __str__(self):
        return f'{self.car_id} {self.service_id}, price: {self.price}€'


class Car(models.Model):
    brand = models.CharField('Brand', max_length=200)
    model = models.CharField('Model', max_length=200)
    engine = models.CharField('Engine capacity', max_length=20)

    def __str__(self):
        return f'{self.brand} {self.model}, {self.engine}'


class Client(models.Model):
    name = models.CharField('Name', max_length=200)
    phone_nr = models.CharField('Phone number', max_length=15)

    def __str__(self):
        return f'{self.name}'


class ClientCar(models.Model):
    client_id = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    car_id = models.ForeignKey('Car', verbose_name='Model', on_delete=models.SET_NULL, null=True)
    year = models.IntegerField('Year', default=2020)
    licence_plate = models.CharField('Licence plate', max_length=10)
    vin_code = models.CharField('VIN code', max_length=15)

    def __str__(self):
        return f'{self.client_id}: {self.car_id}, {self.licence_plate}'


class Order(models.Model):
    client_car_id = models.ForeignKey('ClientCar', verbose_name='Client car', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField('Date')

    def __str__(self):
        return f'{self.client_car_id}, {self.date}'

    STATUS = (
        ('r', 'Draft'),
        ('i', 'In progress'),
        ('d', 'Done'),
        ('c', 'Canceled'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='r',
        help_text='Status',
    )


class OrderLine(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True)
    service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField('Quantity')

    def __str__(self):
        return f'{self.order_id}: {self.service_id}, {self.quantity}'
