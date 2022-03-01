from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def base(request):
    return render (request, 'customerapps/base.html')

def view_customer(request):
    
    customer = Customer.objects.all()
    
    return render(request, 'customerapps/view_customer.html', {'customers':customer})
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            account = Account.objects.get(username=username)
        except:
            return render(request, 'customerapps/login.html', {'warning':'Invalid Login.'})

        if password == account.password:
            return redirect("view_customer" )
        else:
            return render(request, 'customerapps/login.html', {'warning':'Invalid Login.'})
    else:
        return render(request, 'customerapps/login.html')

def logout(request):
    return redirect('/')

def manage_account(request):
    return render(request, 'customersapp/manage_account.html')

def delete_account(request):
    Account.objects.filter().delete()
    return redirect("/")

def create_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            account = Account.objects.get(username=username)
        except:
            Account.objects.create(username=username, password=password)
            message="Account created successfully!"
            return redirect(f"/?message={message}")
        if account:
            return render(request, 'customerapps/create_account.html', {'message':'Account already exists!'})
    else:
        return render(request, 'customerapps/create_account.html')

def add_customer(request):
    customer = Customer.objects.all()
    if(request.method=="POST"):
        Name = request.POST.get('Name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        emailaddress = request.POST.get('emailaddress')
        
        try:
            Customer.objects.create(
                Name=Name, 
                address=address, 
                contact_number=contact_number, 
                emailaddress=emailaddress, 
                )
            return redirect('view_customer')

            return render(request, 'customerapps/add_customer.html', {'message':message, 'customers':customer})

        except Exception as m:
            message = m
            return render(request, 'customerapps/add_customer.html', {'message':message,'customers':customer})
            
    else:
        return render(request, 'customerapps/add_customer.html', {'customers':customer})

def update_customer(request, pk):
    if(request.method=="POST"):
        Name = request.POST.get('Name')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        emailaddress = request.POST.get('emailaddress')
        blank = 0 or '' 
        if Name != blank:
            try:
                Name = Customer.objects.get(Name=Name)
            except:
                Customer.objects.filter(pk=pk).update(Name=Name, emailaddress=emailaddress, contact_number=contact_number)
                return redirect('view_customer')
        else:
            customer = get_object_or_404(Customer, pk=pk)
            message = 'An error occurred. Try again.'
            return render(request, 'customerapps/update_customer.html', {'message': message, 'customers':customer})
    else:
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, 'customerapps/update_customer.html', {'customers':customer})