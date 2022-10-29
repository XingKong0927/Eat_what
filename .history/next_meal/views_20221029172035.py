from django.shortcuts import render

import pandas as pd

# Create your views here.

# decimal转float
def dtf(data_list):
    
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

    # run_log_df = dtf(run_log.objects.all().values())

    return render(request, "powder_tscbys.html", locals())