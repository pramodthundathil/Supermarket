from django.shortcuts import render,redirect
from products.models import Products
from .models import BillCalculations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart

# Create your views here.

@login_required(login_url="SignIn")
def Billing(request):
    product = Products.objects.all()
    bill = BillCalculations.objects.all()
    total = 0
    for item in bill:
        total += int(item.product.Product_unit_Price)
    context = {
        "product":product,
        "bill":bill,
        "total":total,
    }
    return render(request,"Stock/billing.html",context)

@login_required(login_url="SignIn")
def AddBill(request):
    item = request.POST["pname"]
    bach = request.POST['pbatch']
    if Products.objects.filter(Product_Name = item).exists():
        product = Products.objects.get(Product_Name = item)
        bill = BillCalculations.objects.create(product = product,quantity = '1')
        bill.save()
        return redirect("Billing")
    elif Products.objects.filter(Batch_Code = bach).exists():
        product = Products.objects.get(Batch_Code = bach)
        bill = BillCalculations.objects.create(product = product,quantity = '1')
        bill.save()
        return redirect("Billing")
    else:
        messages.info(request,"no item to add")
    
    return redirect(Billing)

@login_required(login_url="SignIn")
def MakeSale(request):
    Bill = BillCalculations.objects.all()
    Bill.delete()
    return redirect('Billing')

@login_required(login_url="SignIn")
def CartView(request):
    cart = Cart.objects.filter(customer  = request.user)
    total = 0
    tax = 0
    for item in cart:
        total += int(item.product.Product_unit_Price)
        tax += int(item.product.GST) 
    
    context = {
        "cart":cart,
        "itemcount" : len(cart),
        "totalbeforetax":(total-tax),
        "total":total,
        "tax":tax
    }
    return render(request,"cart.html",context)
    
@login_required(login_url="SignIn")
def CartAdd(request,pk):
    item = Products.objects.get(id = pk)
    cart = Cart.objects.create(product = item,customer = request.user,itemcount = "1")
    cart.save()
    return redirect('CartView')


@login_required(login_url="SignIn")
def DeleteCart(request,pk):
    cartitem = Cart.objects.get(id = pk)
    cartitem.delete()
    return redirect('CartView')
    
