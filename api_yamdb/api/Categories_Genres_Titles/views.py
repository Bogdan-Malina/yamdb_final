from django.db.models import Avg
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from api.Categories_Genres_Titles.serealizers import (
    CategoriesSerializer,
    GenresSerializer,
    TitlesGetSerializer,
    TitlesPostSerializer
)

from reviews.models import Category, Genre, Title

from api.Categories_Genres_Titles.permissions import AdminOrReadOnly

from api.Categories_Genres_Titles.filters import TitlesFilter


class CategotiesGenresViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class CategoriesViewSet(CategotiesGenresViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    lookup_field = "slug"


class GenresViewSet(CategotiesGenresViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter]
    search_fields = ["name"]
    lookup_field = "slug"


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    )
    serializer_class = TitlesGetSerializer
    permission_classes = [AdminOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesGetSerializer
        return TitlesPostSerializer
