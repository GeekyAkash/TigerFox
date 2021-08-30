from django.db import models

# Create your models here.
class Supplier(models.Model):
    supplier_name =models.CharField(max_length=100)
    supplier_company_name = models.CharField(max_length=150)
    supplier_address =models.CharField(max_length=800)
    supplier_email =models.EmailField(max_length=200)
    supplier_phone =models.IntegerField()
    supplier_message = models.TextField()
    supplier_date =models.DateField()

    def __str__(self):
        return self.supplier_name


class Client(models.Model):
    client_name =models.CharField(max_length=100)
    client_company_name = models.CharField(max_length=200)
    client_address =models.CharField(max_length=800)
    client_email =models.EmailField(max_length=200)
    client_phone =models.IntegerField()
    client_massage = models.TextField()
    client_date =models.DateField()

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    contact_name =models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=150)
    contact_message = models.TextField()
    contact_date =models.DateField()
    
    def __str__(self):
        return self.contact_name