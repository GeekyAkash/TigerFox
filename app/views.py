from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from app.models import Client, Supplier, Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')

def supplier(request):
    if request.method == "POST":
        supplier_name = request.POST.get('supplier_name')
        supplier_company_name = request.POST.get('supplier_company_name')
        supplier_address = request.POST.get('supplier_address')
        supplier_email = request.POST.get('supplier_email')
        supplier_phone = request.POST.get('supplier_phone')
        supplier_message = request.POST.get('supplier_message')
        supplier_date = datetime.today()
        supplier = Supplier(supplier_name = supplier_name, supplier_company_name=supplier_company_name, supplier_address =supplier_address, supplier_email=supplier_email, supplier_phone= supplier_phone, supplier_message=supplier_message, supplier_date = supplier_date) 
        supplier.save()
        messages.success(request, 'Thank you for reaching out to TigerFox. We have received your message and will be in touch within 24 hours.')
    return render(request, 'suppliers.html')

def clients(request):
    if request.method == "POST":
        client_name = request.POST.get('client_name')
        client_company_name = request.POST.get('client_company_name')
        client_address = request.POST.get('client_address')
        client_email = request.POST.get('client_email')
        client_phone = request.POST.get('client_phone')
        client_massage = request.POST.get('client_massage')
        client_date = datetime.today()
        client = Client(client_name=client_name, client_company_name=client_company_name, client_address=client_address, client_email=client_email, client_phone=client_phone, client_massage=client_massage, client_date = client_date)
        client.save()
        messages.success(request, 'Thank you for reaching out to TigerFox. We have received your message and will be in touch within 24 hours.')
    return render(request, 'clients.html')

def contact(request):
    if request.method == "POST":
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_message = request.POST.get('contact_message')
        contact_date = datetime.today()
        contact = Contact(contact_name=contact_name, contact_email=contact_email, contact_message=contact_message, contact_date=contact_date)
        contact.save()
        messages.success(request, 'Thank you for contacting us here at TigerFox. We will be in touch soon. We look forward to serving you.')
    return render(request, 'contact_us.html')