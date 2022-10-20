from django_filters.rest_framework import (
    CharFilter,
    FilterSet,
    NumberFilter
)

from reviews.models import Title


class TitlesFilter(FilterSet):
    category = CharFilter(lookup_expr="slug")
    genre = CharFilter(lookup_expr="slug")
    name = CharFilter(lookup_expr="icontains")
    year = NumberFilter(field_name="year")

    class Meta:
        model = Title
        fields = (
            'name',
            'year',
            'category',
            'genre',
            'description'
        )
