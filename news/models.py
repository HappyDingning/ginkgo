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

# 新闻
class news(models.Model):
    title = models.CharField(max_length = 30, verbose_name = '标题')
    date = models.DateField(verbose_name = '发表日期')
    author = models.CharField(max_length = 20, verbose_name = '作者', null = True, blank = True)
    source = models.CharField(max_length = 20, verbose_name = '来源', null = True, blank = True)
    # text = models.TextField(verbose_name = '正文')
    text = RichTextUploadingField(verbose_name = '正文')
    description = models.CharField(max_length = 200, verbose_name = '描述', null = True, blank = True)
    tag = models.ManyToManyField(tag, verbose_name = '分类')
    cover_img = models.ImageField(verbose_name = '封面', upload_to = 'news_cover', blank = True, null = True, default=None)
    

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = '新闻'

    def __str__(self):
        return self.title
