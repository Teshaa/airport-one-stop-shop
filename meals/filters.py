from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price", lookup_expr='lte')
    type = filters.CharFilter(field_name="type", lookup_expr='name__icontains')
    restaurant = filters.CharFilter(field_name="restaurant")