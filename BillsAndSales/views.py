from django.shortcuts import render,redirect
from products.models import Products
from .models import BillCalculations
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart,CheckoutBill,DeliveryAddress

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
        
    if DeliveryAddress.objects.filter(user = request.user).count() != 0:
        daddress = DeliveryAddress.objects.filter(user = request.user)
    else:
        daddress = [{"Name":"nill"}]
        
    
    context = {
        "cart":cart,
        "itemcount" : len(cart),
        "totalbeforetax":(total-tax),
        "total":total,
        "tax":tax,
        "daddress":daddress
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

@login_required(login_url="SignIn")
def ProceedToCheckOut(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        house = request.POST["house"]
        area = request.POST["area"]
        lmark = request.POST["lmark"]
        
        if DeliveryAddress.objects.filter(user = request.user).exists():
            daddress = DeliveryAddress.objects.get(user = request.user)
            daddress.Name = name
            daddress.phone = phone
            daddress.house = house
            daddress.area = area
            daddress.landmark = lmark
            daddress.save()
        else:
            d = DeliveryAddress.objects.create(Name = name,phone = phone,house = house,area = area,landmark = lmark,user = request.user)
        cart = Cart.objects.filter(customer = request.user)
        for i in cart:
            item = i.product
            cbill = CheckoutBill.objects.create(product = item,customer = request.user)
            cbill.save()
            i.delete()
        
    return render(request,'confirmation.html')


@login_required(login_url="SignIn")
def MyOrders(request):
    context = {'bill':CheckoutBill.objects.filter(customer = request.user)}
    return render(request,"myorders.html",context)
    

