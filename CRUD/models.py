from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

class Product(models.Model):
    productName = models.CharField(max_length=100)
    qty = models.IntegerField()

    # for redirecting
    # create product successfully, but doesn't know where we want to be redirected to
    # tell django how to find the url of a model object is to create get_absolute_url
    # def get_absolute_url(self):
    #    return reverse('crud-home')