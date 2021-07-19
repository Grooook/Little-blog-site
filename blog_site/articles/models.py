from django.db import models
import datetime
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Article title", unique=True, default='')
    text = models.TextField(verbose_name='Article text', default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
 

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name='Comment text', default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'Coment'
        verbose_name_plural = 'Coments'