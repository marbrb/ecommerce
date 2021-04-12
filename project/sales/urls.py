from django.urls import path

from .views import SalesListView
from .views import SaleCreateView
from .views import CreateSaleAjaxView


app_name = 'sales'

urlpatterns = [
    path('', SalesListView.as_view(), name='sales_list'),
    path('nueva/', SaleCreateView.as_view(), name='create_sale'),
    path('nuevagsus/', CreateSaleAjaxView.as_view(), name='create_sale_ajax'),
]
