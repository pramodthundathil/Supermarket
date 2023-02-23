from django.urls import path
from .import views

urlpatterns = [
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("MakeStock",views.MakeStock,name="MakeStock"),
    path("TotalStock",views.TotalStock,name='TotalStock'),
    path("DeleteStock/<int:pk>",views.DeleteStock,name="DeleteStock"),
    path("UpdateItem/<int:pk>",views.UpdateItem,name="UpdateItem"),
    path("ApiProductData",views.ApiProductData,name="ApiProductData")
]
