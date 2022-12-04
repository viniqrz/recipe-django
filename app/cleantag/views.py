from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer
from core.models import Tag
from rest_framework.pagination import PageNumberPagination
# from rest_framework import filters
from django_filters import rest_framework as filters


class ListTagPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10


class ListTagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'status']
        read_only_fields = ['id', 'status']


class ListTagFilter(filters.FilterSet):
    init_date = filters.DateTimeFilter()
    
    class Meta:
        model = Tag
        fields = {
            'name': ['unaccent']
        }

    def get_search_fields(self, view, request):
        return super().get_search_fields(view, request)


class ListTagApi(ListAPIView):
    serializer_class = ListTagSerializer
    queryset = Tag.objects.all()
    pagination_class = ListTagPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ListTagFilter

    def get_queryset(self):
        return self.queryset.filter()
