from django.db import models

# Create your models here.
from django.db import models

class product(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=240, blank=True)
    price = models.IntegerField("Price", max_length=240, blank=True)
    description = models.CharField("Description", max_length=240, blank=True)
    image = models.ImageField(upload_to='photos', max_length=254, blank=True)



    def __str__(self):
        return self.name


class tshirt(models.Model):
    tshirtId = models.AutoField(primary_key=True)
    brand = models.CharField("Brand", max_length=240, blank=True)
    model = models.CharField("Model", max_length=240, blank=True)
    gender = models.CharField("Gender", max_length=240, blank=True)
    price = models.IntegerField("Price", max_length=240, blank=True)
    description = models.CharField("Description", max_length=240, blank=True)
    image = models.ImageField(upload_to='photos', max_length=254, blank=True)


    def __str__(self):
        return self.brand

class shoes(models.Model):
    shoesId = models.AutoField(primary_key=True)
    brand = models.CharField("Brand", max_length=240, blank=True)
    model = models.CharField("Model", max_length=240, blank=True)
    gender = models.CharField("Gender", max_length=240, blank=True)
    price = models.IntegerField("Price", max_length=240, blank=True)
    description = models.CharField("Description", max_length=240, blank=True)
    image = models.ImageField(upload_to='photos', max_length=254, blank=True)

    def __str__(self):
        return self.brand

class sweatshirt(models.Model):
    sweatshirtId = models.AutoField(primary_key=True)
    brand = models.CharField("Brand", max_length=240, blank=True)
    model = models.CharField("Model", max_length=240, blank=True)
    gender = models.CharField("Gender", max_length=240, blank=True)
    price = models.IntegerField("Price", max_length=240, blank=True)
    description = models.CharField("Description", max_length=240, blank=True)
    image = models.ImageField(upload_to='photos', max_length=254, blank=True)

    def __str__(self):
        return self.brand

class jeans(models.Model):
    jeansId = models.AutoField(primary_key=True)
    brand = models.CharField("Brand", max_length=240, blank=True)
    model = models.CharField("Model", max_length=240, blank=True)
    gender = models.CharField("Gender", max_length=240, blank=True)
    price = models.IntegerField("Price", max_length=240, blank=True)
    description = models.CharField("Description", max_length=240, blank=True)
    image = models.ImageField(upload_to='photos', max_length=254, blank=True)

    def __str__(self):
        return self.brand

class bag(models.Model):
    bagId = models.AutoField(primary_key=True)
    brand = models.CharField("Brand", max_length=240, blank=True)
    model = models.CharField("Model", max_length=240, blank=True)
    gender = models.CharField("Gender", max_length=240, blank=True)
    price = models.IntegerField("Price", max_length=240, blank=True)
    description = models.CharField("Description", max_length=240, blank=True)
    image = models.ImageField(upload_to='photos', max_length=254, blank=True)

    def __str__(self):
        return self.brand




