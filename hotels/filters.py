from django_filters import rest_framework as filters


class AccomodationFilter(filters.FilterSet):
    price_min = filters.NumberFilter(field_name="price_per_night", lookup_expr='gte')
    price_max = filters.NumberFilter(field_name="price_per_night", lookup_expr='lte')
    type = filters.CharFilter(field_name="type", lookup_expr='name__icontains')
    tags = filters.CharFilter(
        field_name='feature',
        label="Comma separated Tags",
        method='filter_tags'
    )
    hotel = filters.CharFilter(field_name='hotel')
    def filter_tags(self, queryset, name, value):
        tags = value.strip().split(",")
        return queryset.filter(**{'feature__name__in': tags})
