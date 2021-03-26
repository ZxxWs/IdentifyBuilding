#  建筑物识别系统    

------
本项目只是YOLOv4的UI程序.....


### QT相关参考
1. QTableWidget-[参考链接](https://blog.csdn.net/zhulove86/article/details/52599738?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161623152516780266265586%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161623152516780266265586&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-52599738.first_rank_v2_pc_rank_v29&utm_term=+setEditTriggers)
    
2. dialog、widget、mainwindow的区别-[参考链接](https://blog.csdn.net/weixin_44721961/article/details/88133519?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

3. 信号槽[参考链接](https://blog.csdn.net/u014535666/article/details/104740772?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161633640216780274194659%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161633640216780274194659&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2-104740772.first_rank_v2_pc_rank_v29&utm_term=+pyqtSignal%E6%8E%A5%E6%94%B6)    
    
4. QListView和QListWidget的区别---    
   QListView是基于Model，而QListWidget是基于Item。这是它们的本质区别。


### 问题
> 1. 在导航界面启动主界面的时候，主界面显示一下就闪退。可以将主界面作为导航界面的一个变量。      
> 2. NewProject类的表格改变槽函数可以优化。But懒得弄了
> 3. SettingYoloObjCfg类中的set方法有待优化(文件改写方法)
> 4. mark界面的list文字不能居中，listview长度不能动态控制
> 5. train界面on_pushButtonMove_clicked方法中文件的转存方式有待优化（个人觉得遍历的效率太低
> 6. 变量的作用域以及对程序的影响(这方面知识不会)
> 7. 在执行测试程序的时候（单张图片）不能用绝对路径，应该先到darknet.exe下面。不然会导致/data/labels/下的图片加载不出来的情况。




