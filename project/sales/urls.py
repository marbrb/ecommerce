from django.urls import path

from .views import SalesListView

app_name = 'sales'

urlpatterns = [
    path('', SalesListView.as_view(), name='sales_list'),
]
