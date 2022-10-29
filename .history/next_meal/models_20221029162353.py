from django.db import models

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


menu  
place   
upload_time 
upload_user 
picture  
price

    class Meta:
        db_table = 'menus'  # 表名：菜单
        verbose_name = '菜单'  # 在admin上显示的名字
        verbose_name_plural = verbose_name  # 使单复数形态保持一致