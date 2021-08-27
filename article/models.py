from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# 分类
class tag(models.Model):
    label = models.CharField(max_length = 10, verbose_name = '类别')

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'

    def __str__(self):
        return self.label

# 文章
class article(models.Model):
    title = models.CharField(max_length = 30, verbose_name = '标题')
    date = models.DateField(verbose_name = '发表日期')
    author = models.CharField(max_length = 20, verbose_name = '作者', null = True, blank = True)
    source = models.CharField(max_length = 20, verbose_name = '来源', null = True, blank = True)
    # text = models.TextField(verbose_name = '正文')
    text = RichTextUploadingField(verbose_name = '正文')
    tag = models.ManyToManyField(tag, verbose_name = '分类')   

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title
