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

def random_selection(a):
    """生成随机整数[0, a]"""
    from random import randint
    b = randint(0,a)
    return b

def next_meal0(request):
    """今天吃什么"""
    next_meal = '猜猜今天吃什么？'
    next_meal_picture = 0
    return render(request, "next_meal.html", locals())

def next_meal(request):
    """今天吃什么"""
    menus_df = dtf(menus.objects.all().values())
    random_selection_index = random_selection(len(menus_df)-1)      # 随机选择index
    print("random_selection_index: \n", random_selection_index)

    next_meal = menus_df.loc[random_selection_index, 'menu']
    next_meal_picture = "{}".format(menus_df.loc[random_selection_index, 'picture'])
    next_meal_place = menus_df.loc[random_selection_index, 'place']
    next_meal_price = menus_df.loc[random_selection_index, 'price']
    next_meal_upload_time = menus_df.loc[random_selection_index, 'upload_time']
    next_meal_upload_user = menus_df.loc[random_selection_index, 'upload_user']

    # run_log_df = dtf(run_log.objects.all().values())

    return render(request, "next_meal.html", locals())

"""
    q2_text = request.POST.get('q1_text', '默认查询')
    q2_mode = request.POST.get('q1_mode', '默认方式')

    model = models_dic[q2_mode]
    datalist = model(q2_text)

    return render(request, "Vector_space/home.html", {"data":datalist})
"""