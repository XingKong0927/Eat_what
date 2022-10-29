from django.shortcuts import render

# Create your views here.

def next_meal(request):
    """今天吃什么"""
    return render(request, "powder_tscbys.html", locals())