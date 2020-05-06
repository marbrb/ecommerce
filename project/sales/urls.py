from django.urls import path

from .views import SalesListView
from .views import SaleCreateView


app_name = 'sales'

urlpatterns = [
    path('', SalesListView.as_view(), name='sales_list'),
    path('nueva/', SaleCreateView.as_view(), name='sales_create'),
]
