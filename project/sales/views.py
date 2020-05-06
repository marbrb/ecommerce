from django.views.generic import ListView

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
        for sale in sales:
            total_revenue += sale.revenue

        context['total_revenue'] = total_revenue
        return context
