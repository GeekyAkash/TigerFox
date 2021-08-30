from django.contrib import admin
from app.models import Supplier, Client, Contact
# Register your models here.

admin.site.register(Supplier)
admin.site.register(Client)
admin.site.register(Contact)