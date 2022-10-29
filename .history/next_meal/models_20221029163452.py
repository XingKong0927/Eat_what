from django.db import models
from datetime import datetime

# Create your models here.

class menus(models.Model):  # 菜单
    menu = models.CharField('名称', max_length=100)
    place = models.CharField('地点', max_length=100, default='')
    upload_time = models.DateTimeField('上传时间', default=datetime.now())
    upload_user = models.CharField('上传人', max_length=100, default='')
    picture = models.CharField('图片', max_length=100)
    price = models.DecimalField('价格', max_digits=64, decimal_places=2)

    class Meta:
        db_table = 'menus'  # 表名：菜单
        verbose_name = '菜单'  # 在admin上显示的名字
        verbose_name_plural = verbose_name  # 使单复数形态保持一致

class run_log(models.Model):  # 运行日志
    eat_time = models.DateTimeField('时间', default=datetime.now())
    user_mark = models.CharField('用户标识', max_length=100, default='')
    is_login = models.CharField('是否登陆', max_length=100, default='')
    have_eat = models.CharField('选择结果', max_length=100)

    class Meta:
        db_table = 'run_log'  # 表名：运行日志
        verbose_name = '运行日志'  # 在admin上显示的名字
        verbose_name_plural = verbose_name  # 使单复数形态保持一致

