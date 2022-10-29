from django.contrib import admin
admin.site.site_header = '今天吃什么'
admin.site.site_title = '今天吃什么' 

# Register your models here.
from nxjl.models import financialStatements, materialsPrice, lumpOreCalculation, pulverized_ore_measurement_chart, Vertical_furnace_structure_chart, powder_ore_measurement_chart
from eat_what.models import menus, run_log

class storeFilesAdmin(admin.ModelAdmin):
    # list_display = ["title", "file", "add_time"]
    # list_display = ["file", "add_time"]
    list_display = ["file"]

admin.site.register(menus, storeFilesAdmin)
admin.site.register(run_log, storeFilesAdmin)
admin.site.register(lumpOreCalculation, storeFilesAdmin)

class storeFilesAdmin_fk(admin.ModelAdmin):
    list_display = ["file"]


admin.site.register(pulverized_ore_measurement_chart, storeFilesAdmin_fk)

class storeFilesAdmin_sl(admin.ModelAdmin):
    list_display = ["file"]


admin.site.register(Vertical_furnace_structure_chart, storeFilesAdmin_sl)

class storeFilesAdmin_fk(admin.ModelAdmin):
    list_display = ["file"]


admin.site.register(powder_ore_measurement_chart, storeFilesAdmin_fk)
