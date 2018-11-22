import django_filters

from .models import Word2Vec


class WordsFilter(django_filters.rest_framework.FilterSet):
    """
    word过滤的类
    """
    word = django_filters.CharFilter('word')

    class Meta:
        model = Word2Vec
        fields = [
            'word',
        ]
