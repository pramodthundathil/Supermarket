
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from Home import urls
import Home
import products
from products import urls
from BillsAndSales import urls
import BillsAndSales

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(Home.urls)),
    path("products/",include(products.urls)),
    path("BillsAndSales/",include(BillsAndSales.urls)),
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

