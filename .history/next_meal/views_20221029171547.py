from django.shortcuts import render

# Create your views here.

def next_meal(request):
    """下一餐"""
    return render(request, "powder_tscbys.html", locals())