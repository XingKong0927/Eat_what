from django.shortcuts import render

# Create your views here.

def next_meal(request):
    """铁水成本运算界面加载初始数据"""
    return render(request, "powder_tscbys.html", locals())