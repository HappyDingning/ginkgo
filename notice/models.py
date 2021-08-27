from django.db import models
from ckeditor.fields import RichTextField


# 公告
class notice(models.Model):
    title = models.CharField(max_length = 30, verbose_name = '标题')
    date = models.DateField(verbose_name = '发表日期')
    author = models.CharField(max_length = 20, verbose_name = '作者', null = True, blank = True)
    source = models.CharField(max_length = 20, verbose_name = '来源', null = True, blank = True)
    text = RichTextField(verbose_name = '正文', null = True, blank = True)

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'

    def __str__(self):
        return self.title
