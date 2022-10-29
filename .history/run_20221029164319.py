# -*- coding: utf-8 -*-

import os

# 启动服务器
print("请在浏览器中输入：http://127.0.0.1:8000/login 登录系统")

# 表示将django进程使用的socket绑定ip设置为INADDR_ANY(0)，因此socket会在8000端口监听从本机所有网卡发来的数据，相当于绑定了本机的所有ip地址
# os.system('python manage.py runserver 0.0.0.0:8000 --insecure')
# 表示将socket绑定到本机回环地址，只能监听本机对此服务的请求
os.system('python manage.py runserver 127.0.0.1:8000 --insecure')

