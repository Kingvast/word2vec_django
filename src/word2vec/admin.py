from django.contrib import admin

from .models import Word2Vec


class Word2VecAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'word',
        'vec',
    )
    fields = (
        'word',
        'vec',
    )


admin.site.register(Word2Vec, Word2VecAdmin)
