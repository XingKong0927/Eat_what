'''
数据库初始化方法：
打开命令行：python manage.py shell
复制下方全部代码执行即可
'''
from eat_what.models import menus, run_log

from pandas import read_csv, read_excel
import os
import numpy as np
import pandas as pd



# 初始化数据表1
rmam.objects.create(ID=1001, sinter_name='巴卡', sinter_Fe=65.4, sinter_CaO=0.01,
                    sinter_MgO=0.0268, sinter_SiO2=1.6, sinter_Al2O3=1.26, sinter_P=0.085, sinter_S=0.017, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=6.95, burn_loss=1.5, dry_basis_price_tax=950.09,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1002, sinter_name='金布巴粉', sinter_Fe=60.59, sinter_CaO=0,
                    sinter_MgO=0, sinter_SiO2=4.81, sinter_Al2O3=3.05, sinter_P=0.111, sinter_S=0.024, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=7.68, burn_loss=5.2, dry_basis_price_tax=1240.74,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=5.00,avg_water=8.00,thwd=1300.00,ldxzs=444.00,njxqd=555.00)
rmam.objects.create(ID=1003, sinter_name='65品精粉', sinter_Fe=65.11, sinter_CaO=0.47,
                    sinter_MgO=0.51, sinter_SiO2=5.80, sinter_Al2O3=0.51, sinter_P=0.018, sinter_S=0.573, sinter_K2O=0.076, sinter_Na2O=0.067, sinter_Zn=0.0026,
                    sinter_Pb=0.020, sinter_moisture=10.58, burn_loss=-1.12, dry_basis_price_tax=11083.07,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1004, sinter_name='代县精粉', sinter_Fe=64.50, sinter_CaO=0.8775,
                    sinter_MgO=0.62, sinter_SiO2=7.7, sinter_Al2O3=1.00375, sinter_P=0.036, sinter_S=0.0462, sinter_K2O=0.35, sinter_Na2O=0.06, sinter_Zn=0.0008,
                    sinter_Pb=0.017, sinter_moisture=10.48, burn_loss=-1, dry_basis_price_tax=864.7,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1005, sinter_name='PB粉', sinter_Fe=61.39, sinter_CaO=0.05,
                    sinter_MgO=0.06, sinter_SiO2=3.92, sinter_Al2O3=2.35, sinter_P=0.102, sinter_S=0.021, sinter_K2O=0.0384, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0.02, sinter_moisture=6.93, burn_loss=1.5, dry_basis_price_tax=950.09,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1006, sinter_name='罗伊山粉', sinter_Fe=61.11, sinter_CaO=0.03,
                    sinter_MgO=0.09, sinter_SiO2=3.64, sinter_Al2O3=2.31, sinter_P=0.05, sinter_S=0.02, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=2.4, burn_loss=5, dry_basis_price_tax=831.24,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=6.00,avg_water=8.00,thwd=1200.00,ldxzs=222.00,njxqd=333.00)
rmam.objects.create(ID=1007, sinter_name='纽曼粉', sinter_Fe=62.67, sinter_CaO=0.088,
                    sinter_MgO=0.088, sinter_SiO2=3.71, sinter_Al2O3=2.38, sinter_P=0.1, sinter_S=0.01, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=8, burn_loss=4.2, dry_basis_price_tax=845.27,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1008, sinter_name='超特粉', sinter_Fe=57.17, sinter_CaO=0.07,
                    sinter_MgO=0.08, sinter_SiO2=6.08, sinter_Al2O3=3.39, sinter_P=0.079, sinter_S=0.019, sinter_K2O=0.02, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0.02, sinter_moisture=10.4, burn_loss=8.57, dry_basis_price_tax=1006.23,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1009, sinter_name='巴混粉', sinter_Fe=63.2, sinter_CaO=0,
                    sinter_MgO=0.06, sinter_SiO2=4.8, sinter_Al2O3=1.41, sinter_P=0.07, sinter_S=0.049, sinter_K2O=0.043, sinter_Na2O=0.098, sinter_Zn=0.002,
                    sinter_Pb=0, sinter_moisture=9.31, burn_loss=3.5, dry_basis_price_tax=1281.03,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1010, sinter_name='太钢高硅精粉', sinter_Fe=64.6437, sinter_CaO=0.2998,
                    sinter_MgO=0.6866, sinter_SiO2=4.81, sinter_Al2O3=0.15, sinter_P=0.111, sinter_S=0.2384, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=10.9, burn_loss=1, dry_basis_price_tax=809.77,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1011, sinter_name='FMG混合粉', sinter_Fe=58.5, sinter_CaO=0.02,
                    sinter_MgO=0.08, sinter_SiO2=5.4, sinter_Al2O3=2.44, sinter_P=0.067, sinter_S=0.031, sinter_K2O=0.02, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0.02, sinter_moisture=8.4, burn_loss=7.68, dry_basis_price_tax=998.37,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1012, sinter_name='测试粉', sinter_Fe=0, sinter_CaO=0,
                    sinter_MgO=0, sinter_SiO2=0, sinter_Al2O3=0, sinter_P=0, sinter_S=0, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=0, burn_loss=0, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1101, sinter_name='氧化铁皮', sinter_Fe=68.39, sinter_CaO=1.92,
                    sinter_MgO=0.2, sinter_SiO2=2.67, sinter_Al2O3=0.36, sinter_P=0.1, sinter_S=0, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=6.93, burn_loss=1.5, dry_basis_price_tax=950.09,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1102, sinter_name='高炉除尘灰', sinter_Fe=53, sinter_CaO=11.41,
                    sinter_MgO=2.46, sinter_SiO2=1.23, sinter_Al2O3=2.6, sinter_P=0.13, sinter_S=0.049, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=6, burn_loss=11.3, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1103, sinter_name='高返', sinter_Fe=54.8, sinter_CaO=12.3,
                    sinter_MgO=2.772, sinter_SiO2=5.76, sinter_Al2O3=2.56, sinter_P=0.12, sinter_S=0.08, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=3.05, burn_loss=0.3, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1104, sinter_name='尘泥', sinter_Fe=55, sinter_CaO=5,
                    sinter_MgO=1.82, sinter_SiO2=4, sinter_Al2O3=1, sinter_P=0.1, sinter_S=0.06, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=30, burn_loss=4.48, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1105, sinter_name='国混粉', sinter_Fe=55, sinter_CaO=1.55,
                    sinter_MgO=1.2, sinter_SiO2=5.86, sinter_Al2O3=2.5, sinter_P=0, sinter_S=0, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=6.7, burn_loss=3.15, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1106, sinter_name='磁选粉', sinter_Fe=45.55, sinter_CaO=13.5,
                    sinter_MgO=6.74, sinter_SiO2=8.4166, sinter_Al2O3=1.5266, sinter_P=0, sinter_S=0, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=1, burn_loss=-2, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1201, sinter_name='外购灰', sinter_Fe=0, sinter_CaO=82,
                    sinter_MgO=2.7, sinter_SiO2=2, sinter_Al2O3=1, sinter_P=0.03, sinter_S=0, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=0, burn_loss=8, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1202, sinter_name='回转窑白灰', sinter_Fe=0, sinter_CaO=85,
                    sinter_MgO=4.68, sinter_SiO2=2.3, sinter_Al2O3=0.71, sinter_P=0.03, sinter_S=0.08, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=0, burn_loss=7.8, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1203, sinter_name='白云石粉', sinter_Fe=0, sinter_CaO=32,
                    sinter_MgO=19.65, sinter_SiO2=2, sinter_Al2O3=0.75, sinter_P=0.01, sinter_S=0.07, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=2.12, burn_loss=45, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1204, sinter_name='石灰石粉', sinter_Fe=0, sinter_CaO=50,
                    sinter_MgO=3.7, sinter_SiO2=2.5, sinter_Al2O3=0.6, sinter_P=0.01, sinter_S=0.05, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=1.63, burn_loss=44, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1205, sinter_name='轻烧白云石', sinter_Fe=0, sinter_CaO=64.15,
                    sinter_MgO=24.23, sinter_SiO2=1.88, sinter_Al2O3=0.7, sinter_P=0.01, sinter_S=0.05, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=0, burn_loss=11, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1206, sinter_name='脱硫剂', sinter_Fe=0, sinter_CaO=0,
                    sinter_MgO=0, sinter_SiO2=0, sinter_Al2O3=0, sinter_P=0, sinter_S=0, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=10, burn_loss=0, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1301, sinter_name='自返焦粉', sinter_Fe=0, sinter_CaO=0.78,
                    sinter_MgO=0.39, sinter_SiO2=7.84, sinter_Al2O3=5.61, sinter_P=0.06, sinter_S=0.99, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=10, burn_loss=82.87, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)
rmam.objects.create(ID=1302, sinter_name='无烟煤', sinter_Fe=0, sinter_CaO=0.94,
                    sinter_MgO=0.21, sinter_SiO2=7.5, sinter_Al2O3=3, sinter_P=0.07, sinter_S=0.63, sinter_K2O=0, sinter_Na2O=0, sinter_Zn=0,
                    sinter_Pb=0, sinter_moisture=10, burn_loss=82.87, dry_basis_price_tax=0,
                    wet_ton_price_tax_included=0,wet_ton_price_tax_excluded=0,avg_size=0,avg_water=8.00,thwd=0,ldxzs=0,njxqd=0)


# 初始化数据表2
ftable.objects.create(ID=8, input_materials_name='烧结矿', input_materials_Fe=0.654, input_materials_S=0.0001, input_materials_SiO2=0.044, input_materials_CaO=0.0009,
                      input_materials_MgO=0.0004, input_materials_Al2O3=0.0103, heap_weight=2.3, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=1, input_materials_name='南非块', input_materials_Fe=0.654, input_materials_S=0.0001, input_materials_SiO2=0.044, input_materials_CaO=0.0009,
                      input_materials_MgO=0.0004, input_materials_Al2O3=0.0103, heap_weight=2.3, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=2, input_materials_name='伊朗球', input_materials_Fe=0.647, input_materials_S=0.0001, input_materials_SiO2=0.033, input_materials_CaO=0.0058,
                      input_materials_MgO=0.0196, input_materials_Al2O3=0.0059, heap_weight=2, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=3, input_materials_name='巴西筛后', input_materials_Fe=0.6246, input_materials_S=0.0003, input_materials_SiO2=0.071, input_materials_CaO=0.0001,
                      input_materials_MgO=0.0006, input_materials_Al2O3=0.0198, heap_weight=1.5, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=4, input_materials_name='罗伊山', input_materials_Fe=0.6139, input_materials_S=0, input_materials_SiO2=0.0473, input_materials_CaO=0.0004,
                      input_materials_MgO=0.0005, input_materials_Al2O3=0.0195, heap_weight=2, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=5, input_materials_name='硅石', input_materials_Fe=0, input_materials_S=0, input_materials_SiO2=0.8198, input_materials_CaO=0, input_materials_MgO=0,
                      input_materials_Al2O3=0, heap_weight=1.5, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=6, input_materials_name='国内球团矿', input_materials_Fe=0.625, input_materials_S=0, input_materials_SiO2=0.073, input_materials_CaO=0.001, input_materials_MgO=0.002,
                      input_materials_Al2O3=0.0072, heap_weight=1.5, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)
ftable.objects.create(ID=7, input_materials_name='白云石', input_materials_Fe=0, input_materials_S=0, input_materials_SiO2=0, input_materials_CaO=0.3094, input_materials_MgO=0.2066,
                      input_materials_Al2O3=0, heap_weight=1.5, powder_ratio=0.3, dry_basis_price_tax=1000, wet_ton_price_tax_included=800, wet_ton_price_tax_excluded=900)

'''初始化训练数据库'''

# 读数据源
df = read_csv('C:\\Users\\Admin\Desktop\\mine\\Intelligent-ore-blending\\data\\data_preprocess\\250+20烧结杯整合数据.csv')

for i in range(len(df)):
    for j in list(df):
        if pd.isnull(df.at[i,j]):
            df.loc[i,j] = 0
print(df)
# df.to_excel('C:\\Users\\Admin\\Desktop\\df输出测试.xlsx')
# 改表名，把传的参数改成要填进去的数
try:
    for i in range(len(df)):
        prediction_data.objects.create(name='default', baka=df.loc[i]['baka'], chaote=df.loc[i]['chaote'], yindu=df.loc[i]['yindu'], luoyishan=df.loc[i]['luoyishan'], jinbuba=df.loc[i]['jinbuba'], maike=df.loc[i]['maike'], bahun=df.loc[i]['bahun'], gaofan=df.loc[i]['gaofan'], chenni=df.loc[i]['chenni'], cixuan=df.loc[i]['cixuan'], baihui=df.loc[i]['baihui'], qingshao=df.loc[i]['qingshao'], baiyunshi=df.loc[i]['baiyunshi'], shihui=df.loc[i]['shihui'], jiaofen=df.loc[i]['jiaofen'], wuyanmei=df.loc[i]['wuyanmei'], fmg=df.loc[i]['fmg'], sp10=df.loc[i]['sp10'], pb=df.loc[i]['pb'], jingfen=df.loc[i]['jingfen'], luobuhe=df.loc[i]['luobuhe'], diaoyan=df.loc[i]['diaoyan'], huanjinghui=df.loc[i]['huanjinghui'], yanghuatiepi=df.loc[i]['yanghuatiepi'], zhonglihui=df.loc[i]['zhonglihui'], burn_loss=df.loc[i]['burn_loss'], mixture_moisture=df.loc[i]['mixture_moisture'], fire_temperature=df.loc[i]['fire_temperature'], fire_pressure=df.loc[i]['fire_pressure'], material_thickness=df.loc[i]['material_thickness'], sinter_pressure=df.loc[i]['sinter_pressure'], end_temperature=df.loc[i]['end_temperature'], sinter_time=df.loc[i]['sinter_time'], systolic_rate=df.loc[i]['systolic_rate'], vertical_speed=df.loc[i]['vertical_speed'], sinter_40mm=df.loc[i]
                                       ['>=40mm'], sinter_25_40mm=df.loc[i]['25-40mm'], sinter_16_25mm=df.loc[i]['16-25mm'], sinter_10_16mm=df.loc[i]['10-16mm'], sinter_5_10mm=df.loc[i]['5-10mm'], sinter_5mm=df.loc[i]['<=5mm'], average_size_sinter=df.loc[i]['average_size_sinter'], finish_product_rate=df.loc[i]['finish_product_rate'], reore_rate=df.loc[i]['reore_rate'], conversion_index=df.loc[i]['conversion_index'], sinter_TFe=df.loc[i]['sinter_TFe'], sinter_FeO=df.loc[i]['sinter_FeO'], sinter_SiO2=df.loc[i]['sinter_SiO2'], sinter_CaO=df.loc[i]['sinter_CaO'], sinter_MgO=df.loc[i]['sinter_MgO'], sinter_Al2O3=df.loc[i]['sinter_Al2O3'], sinter_P=df.loc[i]['sinter_P'], sinter_S=df.loc[i]['sinter_S'], sinter_MnO=df.loc[i]['sinter_MnO'], sinter_TiO2=df.loc[i]['sinter_TiO2'], sinter_V2O5=df.loc[i]['sinter_V2O5'], R=df.loc[i]['R'], mix_Fe=df.loc[i]['mix_Fe'], mix_CaO=df.loc[i]['mix_CaO'], mix_MgO=df.loc[i]['mix_MgO'], mix_SiO2=df.loc[i]['mix_SiO2'], mix_Al2O3=df.loc[i]['mix_Al2O3'], mix_P=df.loc[i]['mix_P'], mix_S=df.loc[i]['mix_S'], mix_moisture=df.loc[i]['mix_moisture'], mix_C=df.loc[i]['mix_C'], mix_K2O=df.loc[i]['mix_K2O'], mix_Na2O=df.loc[i]['mix_Na2O'], mix_Zn=df.loc[i]['mix_Zn'], mix_Pb=df.loc[i]['mix_Pb'], sinter_10_40mm=df.loc[i]['10_40mm'])
    print(i)
    print('存训练数据库成功')
except Exception as e:
    print('存训练数据库错误：', e)

'''初始化预测界面'''
linshi_canshu.objects.create(name='风机频率', ratio=50)
linshi_canshu.objects.create(name='料层厚度', ratio=70)
linshi_canshu.objects.create(name='机速', ratio=23)
linshi_canshu.objects.create(name='混料时间', ratio=6)
linshi_canshu.objects.create(name='加水量(率)', ratio=7)
linshi_canshu.objects.create(name='点火时间', ratio=120)
linshi_canshu.objects.create(name='点火负压', ratio=15)

'''初始化配矿界面'''
yuanliao_choose.objects.create(name='巴卡', ratio=0, max=14, min=12)
yuanliao_choose.objects.create(name='65品精粉', ratio=0, max=20, min=20)
yuanliao_choose.objects.create(name='超特粉', ratio=0, max=18, min=18)
yuanliao_choose.objects.create(name='FMG混合粉', ratio=0, max=15, min=15)
yuanliao_choose.objects.create(name='氧化铁皮', ratio=0, max=0.7, min=0.7)
yuanliao_choose.objects.create(name='高炉除尘灰', ratio=0, max=0.8, min=0.8)
yuanliao_choose.objects.create(name='高返', ratio=0, max=11.5, min=11.5)
yuanliao_choose.objects.create(name='尘泥', ratio=0, max=1.5, min=1.5)
yuanliao_choose.objects.create(name='磁选粉', ratio=0, max=1.23, min=1.23)
yuanliao_choose.objects.create(name='回转窑白灰', ratio=0, max=5.5, min=5.5)
yuanliao_choose.objects.create(name='白云石粉', ratio=0, max=7, min=6)
yuanliao_choose.objects.create(name='石灰石粉', ratio=0, max=3, min=2)
yuanliao_choose.objects.create(name='自返焦粉', ratio=0, max=4, min=4)

ftable_choose.objects.create(name='烧结矿',ratio=77)
ftable_choose.objects.create(name='南非块',ratio=5)
ftable_choose.objects.create(name='国内球团矿',ratio=18)

sinter_xianding.objects.create(name='碱度', max=1.4, min=1.2)
sinter_xianding.objects.create(name='镁铝比', max=0.8, min=0.6)
sinter_xianding.objects.create(name='P', max=1, min=1)
sinter_xianding.objects.create(name='Al', max=0.032, min=0.02)
sinter_xianding.objects.create(name='Mg', max=0.4, min=0.023)
sinter_xianding.objects.create(name='Ca', max=0.13, min=0.09)
sinter_xianding.objects.create(name='Si', max=0.07, min=0.05)
sinter_xianding.objects.create(name='Fe', max=0.56, min=0.53)

peikuang_lingsan.objects.create(name='步长',ratio=0.1)
peikuang_lingsan.objects.create(name='tax_rate',ratio=0.001)
peikuang_lingsan.objects.create(name='power_cost',ratio=35.174)
peikuang_lingsan.objects.create(name='wage_surcharge',ratio=6.835)
peikuang_lingsan.objects.create(name='manufacturing_cost',ratio=27.164)

peikuang_jiaoding_meifen.objects.create(fuels_name='焦丁',fuels_weight=300,fuels_moisture=0.04,fuels_ash=0.131,ash_SiO2=0.4961,ash_CaO=0.0529,ash_S=0.0066,ash_MgO=0.0288,ash_Al2O3=0.36,id=0)
peikuang_jiaoding_meifen.objects.create(fuels_name='煤粉',fuels_weight=3000,fuels_moisture=0.0,fuels_ash=0.1084,ash_SiO2=0.4188,ash_CaO=0.06,ash_S=0.0,ash_MgO=0.0115,ash_Al2O3=0.36,id=0)

# yuanliao_choose
# linshi_hunheliao







