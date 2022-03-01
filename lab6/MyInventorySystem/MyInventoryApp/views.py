# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def main(request):
    return render(request, 'MyInventoryApp/main.html')
    
def view_supplier(request, pk):
    create = Account.objects.get(pk=pk)
    supplier = Supplier.objects.all()
    
    return render(request, 'MyInventoryApp/view_supplier.html', {'suppliers':supplier, 'create':create})

def view_bottles(request, pk):
    create = Account.objects.get(pk=pk)
    bottle = WaterBottle.objects.all()
    if request.GET.get('message') == None:
        message = ""
    else:
        message = request.GET.get('message')
        
    return render(request, 'MyInventoryApp/view_bottles.html', {'bottles':bottle, 'message':message, 'create':create})

def view_bottle_details(request, pk):
    bottle = get_object_or_404(WaterBottle, pk=pk)
    url = request.META.get('HTTP_REFERER')
    request.session['url'] = url
    print(url)
    
    return render(request, 'MyInventoryApp/view_bottle_details.html', {'bottle':bottle})

def add_bottle(request):
    supplier = Supplier.objects.all()
    if(request.method=="POST"):
        SKU = request.POST.get('SKU')
        brand = request.POST.get('brand')
        cost = request.POST.get('cost')
        size = request.POST.get('size')
        mouth_size= request.POST.get('mouth_size')
        color = request.POST.get('color')
        supplier = request.POST.get('supplier')
        current_quantity = request.POST.get('current_quantity')
        
        try:
            WaterBottle.objects.create(
                SKU=SKU, 
                brand=brand, 
                cost=cost, 
                size=size, 
                mouth_size=mouth_size, 
                color=color, 
                supplier=Supplier.objects.get(id=supplier), 
                current_quantity=current_quantity,
                )
            message = "Bottle successfully added"
            return render(request, 'MyInventoryApp/add_bottle.html', {'message':message, 'suppliers':supplier})

        except Exception as m:
            message = m
            return render(request, 'MyInventoryApp/add_bottle.html', {'message':message, 'suppliers':supplier})
            
    else:
        return render(request, 'MyInventoryApp/add_bottle.html', {'suppliers':supplier})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            account = Account.objects.get(username=username)
        except:
            return render(request, 'MyInventoryApp/login.html', {'message':'Invalid Login'})

        if password == account.password:
            return redirect("view_supplier", pk=account.pk)
        else:
            return render(request, 'MyInventoryApp/login.html', {'message':'Invalid Login'})

    else:
        if request.GET.get('message') == None:
            context = {'message': ''}
        else:
            context = {'message':request.GET.get('message')}
        return render(request, 'MyInventoryApp/login.html', context)

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            account = Account.objects.get(username=username)
        except:
            Account.objects.create(username=username, password=password)
            message="Account created successfully"
            return redirect(f"/?message={message}")

        if account:
            return render(request, 'MyInventoryApp/signup.html', {'message':'Account already exists'})

    else:
        return render(request, 'MyInventoryApp/signup.html', {'message':''})


def manage_account(request, pk):
    create = get_object_or_404(Account, pk=pk)
    if request.GET.get('message') == None:
        context = {'create':create, 'message': ''}
    else:
        context = {'create':create, 'message':request.GET.get('message')}
    return render(request, 'MyInventoryApp/manage_account.html', context)

def logout(request):
    return redirect('/')

def delete_user(request, pk):
    create = get_object_or_404(Account, pk=pk)
    Account.objects.filter(pk=pk).delete()
    return redirect('/')

def delete_bottle(request, pk):
    details = get_object_or_404(WaterBottle, pk=pk)
    WaterBottle.objects.filter(pk=pk).delete()
    
    url = request.session['url']
    return redirect(f"{url}")


def change_password(request, pk):
    create = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        new1_password = request.POST.get('new1_password')

        if current_password == create.password and new_password == new1_password and current_password != new_password:
            Account.objects.filter(pk=pk).update(password=new1_password)
            message = request.POST.get('message')
            return redirect(f'/manage_account/{pk}/?message={message}', pk=pk)
        
        else:
            return render(request, 'MyInventoryApp/change_password.html', {'create':create, 'message':'An Error Occured'})
    else:
        return render(request, 'MyInventoryApp/change_password.html', {'create': create})