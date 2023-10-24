import django_filters
from .models import Product, Manufacturer


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Мин.цена:', required=False)
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Макс.цена:', required=False)
    manufacturer = django_filters.ModelChoiceFilter(queryset=Manufacturer.objects.all(), label='Производитель:', empty_label="Выберите производителя", required=False)

    class Meta:
        model = Product
        fields = []
