from django.db import models


class Order(models.Model):
    title = models.CharField(max_length=120)  # max length required
    price = models.DecimalField(decimal_places=2, max_digits=99, default=0.00)
    isDiscounted = models.BooleanField(default=True)
