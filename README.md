# Eat_what
今天吃什么？  适用于不知道下一餐吃什么的大学生们



## 项目需求

1. 随机选择某样食物；
2. 可以上传食物



## 数据库-Eatwhat

1. 菜单-menus

|  名称  |   地点   |  上传时间   |   上传人    |   图片   | 价格  |
| :----: | :------: | :---------: | :---------: | :------: | :---: |
|  menu  |  place   | upload_time | upload_user | picture  | price |
| 香锅面 | 梅园食堂 |             |   用户名    | 图片地址 |  10   |

2. 运行日志-run_log

|   时间   | 用户标识  | 是否登陆  | 选择结果 |
| :------: | :-------: | :-------: | :------: |
| eat_time | user_mark | is_login  | have_eat |
|          | 设备标识  | 用户名/否 |  香锅面  |

