from django.db import models
from datetime import datetime

# Create your models here.

class menus(models.Model):  # 菜单
    plan_id = models.IntegerField('方案id', default=-1)
    base_power_price = models.DecimalField('基准粉价格', max_digits=64, decimal_places=4, default=0.0)
    base_power_grade = models.DecimalField('基准粉品位', max_digits=64, decimal_places=4, default=0.0)
    base_power_Si = models.DecimalField('基准粉硅', max_digits=64, decimal_places=4, default=0.0)
    single_grade_price_difference = models.DecimalField('单品位价差', max_digits=64, decimal_places=4, default=0.0)
    single_Si_price_difference = models.DecimalField('单硅价差', max_digits=64, decimal_places=4, default=0.0)

    kind = models.CharField('所属模块（矿粉/预测/配矿）', max_length=100, default='')
    user = models.CharField('用户', max_length=100, default='')

    menu = models.CharField('名称', )
    place = models.CharField('地点', )
    upload_time = models.DateTimeField('上传时间', default=datetime.now())
    upload_user = models.CharField('上传人', )
    picture = models.CharField('图片', )
    price = models.DecimalField('价格', )

    class Meta:
        db_table = 'menus'  # 表名：菜单
        verbose_name = '菜单'  # 在admin上显示的名字
        verbose_name_plural = verbose_name  # 使单复数形态保持一致

| eat_time | user_mark | is_login  | have_eat
|   时间   | 用户标识  | 是否登陆  | 选择结果