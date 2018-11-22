from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination

from .filters import WordsFilter
from .models import Word2Vec
from .serializers import Word2VecSerializer


class Word2VecPagination(PageNumberPagination):
    """
    列表自定义分页
    """
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'


class Word2VecListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pagination_class = Word2VecPagination
    queryset = Word2Vec.objects.all().order_by('id')
    serializer_class = Word2VecSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = WordsFilter
    search_fields = ('word', )
