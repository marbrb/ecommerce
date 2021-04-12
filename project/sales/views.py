import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import View

from products.models import Product

from .services import get_calculated_sale_values
from .services import update_stock
from .forms import SaleForm
from .models import Sale


class SalesListView(ListView):
    model = Sale
    template_name = 'sales_list.html'
    context_object_name = 'sales'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sales = self.get_queryset()

        total_revenue = 0
        total_purchase_amount = 0
        total_sale_amount = 0
        for sale in sales:
            total_revenue += sale.revenue
            total_purchase_amount += sale.total_purchase_amount
            total_sale_amount += sale.total_sale_amount

        context['total_revenue'] = total_revenue
        context['total_purchase_amount'] = total_purchase_amount
        context['total_sale_amount'] = total_sale_amount
        return context


class SaleCreateView(CreateView):
    model = Sale
    template_name = 'sales_form.html'
    form_class = SaleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CreateSaleAjaxView(View):
    def post(self, request, *args, **kwargs):
        products_data = json.loads(request.body)
        form = SaleForm({'products': products_data})
        if form.is_valid():
            sale = form.save(commit=False)
            total_purchase_amount, total_sale_amount = \
                get_calculated_sale_values(products_data)

            sale.total_purchase_amount = total_purchase_amount
            sale.total_sale_amount = total_sale_amount

            sale.save()

            update_stock(sale)
        else:
            print(form.errors)
            return JsonResponse({
                'ok': False,
                'message': 'Falló la creación'
            })

        return JsonResponse({
            'ok': True
        })
