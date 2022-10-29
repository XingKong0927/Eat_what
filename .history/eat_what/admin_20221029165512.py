from django.contrib import admin
admin.site.site_header = '今天吃什么'
admin.site.site_title = '今天吃什么' 

# Register your models here.
from nxjl.models import financialStatements, materialsPrice, lumpOreCalculation, pulverized_ore_measurement_chart, Vertical_furnace_structure_chart, powder_ore_measurement_chart
from eat_what.models import menus, run_log

class storeFilesAdmin1(admin.ModelAdmin):
    list_display = ["menu", "place", "upload_time", "upload_user", "picture", "price"]

class storeFilesAdmin2(admin.ModelAdmin):
    list_display = ["file"]

admin.site.register(menus, storeFilesAdmin1)
admin.site.register(run_log, storeFilesAdmin2)
