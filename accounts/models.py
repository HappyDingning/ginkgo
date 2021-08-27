from django.db import models
from django.contrib.auth.models import User

# 用户扩展信息
class user_profile(models.Model):
    user = models.OneToOneField(User, verbose_name = '关联账户', on_delete = models.SET_NULL, null=True, blank = True)
    name = models.CharField(max_length = 5, verbose_name = '姓名')
    email = models.CharField(max_length = 254, verbose_name = '电子邮箱', unique=True, null = True, blank = True)
    identity = models.IntegerField(verbose_name = '身份', choices = ((0, "教师"), (1, "学生")))
    student_id = models.CharField(max_length = 11, verbose_name = '学号', unique=True, null = True, blank = True)
    user_class = models.CharField(max_length = 20, verbose_name = '专业班级', null = True, blank = True)
    telephone = models.IntegerField(verbose_name = '电话', unique=True, null = True, blank = True)
    duty = models.IntegerField(verbose_name = '职务', choices = ((1, "总负责人"), (2, "负责人"), (3, "指导老师"),
                                                                 (4, "管理人员"), (5, "往届队长"), (6, "团支部书记"),
                                                                 (7, "宣传部长"), (8, "技术培训部长"), (9, "组织部长"),
                                                                 (10, "超算基地正式成员"), (11, "超算预备队员"), (12, "超算爱好者")))
    introduction = models.TextField(verbose_name = '个人介绍', null = True, blank = True)
    edit_date = models.DateField(verbose_name = '编辑日期', auto_now = True)
    is_shown = models.BooleanField(verbose_name = '在成员列表中展示', default = False)
    photo = models.ImageField(verbose_name = '头像', upload_to = 'photo', blank = True, null = True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.name

# 报名申请
class application(models.Model):
    name = models.CharField(max_length = 5, verbose_name = '姓名')
    email = models.CharField(max_length = 254, verbose_name = '电子邮箱', unique=True, null = True, blank = True)
    student_id = models.CharField(max_length = 11, verbose_name = '学号', unique=True, null = True, blank = True)
    user_class = models.CharField(max_length = 20, verbose_name = '专业班级', null = True, blank = True)
    date = models.DateField(verbose_name = '提交时间', auto_now_add = True)
    major = models.IntegerField(verbose_name = '方向', choices = ((1, '统招'), (2, '宣传')))

    class Meta:
        verbose_name = '报名申请'
        verbose_name_plural = '报名信息'

    def __str__(self):
        return '第%d号申请'%self.id
