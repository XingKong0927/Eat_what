from django.shortcuts import render

# Create your views here.

def next_meal(request):
    """今天吃什么"""
    menus_df = menus.objects.all().values()
    run_log_df = run_log.objects.all().values()
    return render(request, "powder_tscbys.html", locals())