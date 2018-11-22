from django.db import models


class Word2Vec(models.Model):
    word = models.CharField('单词', max_length=64)
    vec = models.TextField('词向量', default='')
