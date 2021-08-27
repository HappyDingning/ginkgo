from django.db import models
from news.models import news

class achievement(models.Model):
    title = models.CharField(max_length = 30, verbose_name = '标题')
    outline = models.CharField(max_length = 200, null = True, blank = True, verbose_name = '概述')
    date = models.DateField(verbose_name = '获奖日期')
    members = models.CharField(max_length = 100, null = True, blank = True, verbose_name = '参加成员')
    counselor = models.CharField(max_length = 100, null = True, blank = True, verbose_name = '指导老师')
    level = models.IntegerField(verbose_name = 'level', default = 0)
    news = models.ForeignKey(news, on_delete = models.SET_NULL, null=True, blank = True, verbose_name = '关联新闻')

    class Meta:
        verbose_name = '成就'
        verbose_name_plural = '成就'

    def __str__(self):
        return self.title
