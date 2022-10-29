from django.shortcuts import render
from eat_what.models import menus, run_log
import pandas as pd

# Create your views here.

def dtf(data_list):
    """数据库数据转为dataframe，decimal转float
    """
    for dic in data_list:
        for i in dic:
            try:
                if  i == 'id':
                    pass
                else:
                    dic[i] = float(dic[i])
            except:pass
    df = pd.DataFrame(list(data_list))    #转为dataframe
    return df

def next_meal(request):
    """今天吃什么"""
    menus_df = dtf(menus.objects.all().values())
    print("menus_df: \n", menus_df)

    next_meal = menus_df.loc[0, 'menu']

    # run_log_df = dtf(run_log.objects.all().values())

    return render(request, "next_meal.html", locals())

"""
    q2_text = request.POST.get('q1_text', '默认查询')
    q2_mode = request.POST.get('q1_mode', '默认方式')

    model = models_dic[q2_mode]
    datalist = model(q2_text)

    return render(request, "Vector_space/home.html", {"data":datalist})
"""