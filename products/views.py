from django.shortcuts import render,redirect
from .forms import ProductAddForm,Venderaddfrom
from django.contrib import messages
from .models import Products,Venders
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from BillsAndSales.models import BillId
# Create your views here.
def AdminHome(request):
    context= {
        "stocktotal": Products.objects.all().count(),
        "TotalSale": BillId.objects.all().count(),
        'venders':len(Venders.objects.all())
    }
    return render(request,"Stock/adminhome.html",context)

def MakeStock(request):
    form = ProductAddForm
    if request.method =="POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"New stock Added")
            return redirect('MakeStock')
    context = {
        "form":form
    }
    return render(request,"Stock/updatestock.html",context)

def TotalStock(request):
    stock = Products.objects.all()
    context = {
        "stock":stock
    }
    return render(request,"Stock/stock.html",context)

@api_view(['GET'])
def ApiProductData(request):
    product = Products.objects.all()
    serializer = ProductSerializer(product,many = True)
    return Response(serializer.data)

def DeleteStock(request,pk):
    item = Products.objects.get(id = pk)
    item.delete()
    messages.info(request,"Item Removed from stock")
    return redirect("TotalStock")

def UpdateItem(request,pk):
    item = Products.objects.get(id =pk)
    messages.info(request," {} is not Possible to Update Now. Please delete the item and try to add a new item".format(item))
    return redirect("TotalStock")

def VenderPage(request):
    form  = Venderaddfrom()
    ven = Venders.objects.all()
    if request.method == "POST":
        form = Venderaddfrom(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Vender Added success")
            return redirect('VenderPage')
    context = {
        "form":form,
        "ven":ven
    }
    return render(request,"Stock/venderadd.html",context)

def DeleteVender(request,pk):
    Venders.objects.get(id = pk).delete()
    messages.info(request,"Vender Deleted")
    return redirect('VenderPage')
    