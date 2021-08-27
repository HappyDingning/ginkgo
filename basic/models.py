from django.db import models

class carousel(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    img_filename = models.ImageField(max_length = 255, verbose_name = '封面图片')
    title = models.CharField(max_length = 20, verbose_name = '标题')
    description = models.CharField(max_length = 100, verbose_name = '描述')
    link = models.CharField(max_length = 50, verbose_name = '文本编号')
    content_class = models.IntegerField(verbose_name = '内容类别', choices = ((1, "基地介绍"), (2, "新闻"), (3, "指导老师"),
                                                                 (4, "成员"), (5, "公告"), (6, "文章"),
                                                                 (7, "关于我们"), (8, "保留"), (9, "保留"),))
    place = models.IntegerField(verbose_name = '安放位置', choices = ((1, "顶端"), (2, "中部")))

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return '第%d号轮播图'%self.id
