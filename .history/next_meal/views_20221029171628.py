from django.shortcuts import render

# Create your views here.

def next_meal(request):
    """今天吃什么"""
    rmam_df = rmam.objects.all().values()
    return render(request, "powder_tscbys.html", locals())