from django.db import models

class Products(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="img/%y")
    description=models.CharField(max_length=200)
    price=models.IntegerField(null=True)

class SayCustomer(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="img/%y")
    feedback=models.CharField(max_length=200)

class News(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    author=models.CharField(max_length=50)
    dateSubmitted=models.DateField()
    description=models.CharField(max_length=200)
