from django.shortcuts import render
from eat_what.models import menus, run_log

import pandas as pd

from django.contrib import messages

def dtf(data_list):
    """数据库数据转为dataframe，decimal转float
    """
    for dic in data_list:
        for i in dic:
            try:
                if(i == 'price'):
                    dic[i] = float(dic[i])
            except:pass
    df = pd.DataFrame(list(data_list))    #转为dataframe
    return df

def random_selection(a):
    """生成随机整数[0, a]"""
    from random import randint
    b = randint(0,a)
    return b

def next_meal(request):
    """今天吃什么"""
    menus_df0 = dtf(menus.objects.all().values())
    if request.method == 'GET':
        next_meal = '猜猜今天吃什么？'
        next_meal_picture = 0
        dining_place_list = list(menus_df0['place'])     # 就餐地点罗列
    else:
        dining_places = request.POST.getlist('dining_places')
        if dining_places:       # 选择了地点
            menus_df = menus_df0[menus_df0["place"].isin(dining_places)]        # 根据list筛选数据
            menus_df = menus_df.reset_index(drop=True)                          # 重置索引
        else:                   # 没有选择地点
            menus_df = menus_df0
        random_selection_index = random_selection(len(menus_df)-1)      # 随机选择index

        next_meal = menus_df.loc[random_selection_index, 'menu']
        next_meal_picture = "{}".format(menus_df.loc[random_selection_index, 'picture'])
        next_meal_place = menus_df.loc[random_selection_index, 'place']
        next_meal_price = menus_df.loc[random_selection_index, 'price']
        next_meal_upload_time = menus_df.loc[random_selection_index, 'upload_time']
        next_meal_upload_time = next_meal_upload_time.strftime("%Y-%m-%d")      # '%Y %m %d %H:%M:%S'
        print("next_meal_upload_time: ", next_meal_upload_time)
        next_meal_upload_user = menus_df.loc[random_selection_index, 'upload_user']
        dining_place_list = list(menus_df0['place'])     # 就餐地点罗列

        login_user = str(request.user)
        is_login0 = request.user.is_authenticated
        run_log.objects.create(user_mark=login_user, is_login=is_login0, have_eat=next_meal)       # 录入到数据库

    return render(request, "next_meal.html", locals())

def enter_meal(request):
    """食物录入"""
    if request.method == 'GET':
        return render(request, "enter_meal.html")
    else:
        # 保存文件
        menu_name = str(request.POST.get('menu_name'))
        menus_df = dtf(menus.objects.all().values())
        menus_list = list(menus_df['menu'])

        if(menu_name in menus_list):                    # 查重
            messages.error(request, '美食【{}】已存在，录入失败'.format(menu_name))
        else:
            login_user = str(request.user)
            
            file = request.FILES['picpath']     # 获取一个文件管理器对象
            # 将要保存的地址和文件名称
            where = 'eat_what/static/Picture/{}.jpg'.format(menu_name)
            # 分块保存image
            content = file.chunks()
            with open(where, 'wb') as f:
                for i in content:
                    f.write(i)
            menu_place = str(request.POST.get('menu_place'))
            menu_price = request.POST.get('menu_price')

            menus.objects.create(menu=menu_name, place=menu_place, upload_user=login_user, picture=menu_name, price=menu_price)       # 录入到数据库
            messages.success(request, '美食【{}】录入成功'.format(menu_name))
        menus_df = dtf(menus.objects.all().values())
        # print("menus_df: \n", menus_df)
        return render(request, "enter_meal.html")
