from django.urls import path
from .import views

urlpatterns = [
    path("Billing",views.Billing,name="Billing"),
    path("AddBill",views.AddBill,name="AddBill"),
    path("MakeSale",views.MakeSale,name="MakeSale"),
    path("CartView",views.CartView,name="CartView"),
    path("CartAdd/<int:pk>",views.CartAdd,name="CartAdd"),
    path("DeleteCart/<int:pk>",views.DeleteCart,name="DeleteCart"),
    path("ProceedToCheckOut",views.ProceedToCheckOut,name="ProceedToCheckOut"),
    path("MyOrders",views.MyOrders,name="MyOrders")
]
