# AutoReport

北京化工大学疫情上报，仅在正常情况下使用。

# 使用方法：

## Fiddler对企业微信进行抓包

### 1. 打开Fiddler，Tools—>Options，设置如下：

![image-20200630142457401](https://i.loli.net/2020/06/30/2Djra8tCszilpgO.png)

### 2. 打开企业微信，进入疫情防控上报页面

![image-20200630142616244](https://i.loli.net/2020/06/30/MTWDeO3p1wjSNsn.png)

### 3.找到Cookie值，找到`eai-sess`和`UUkey`

![image-20200630143137490](https://i.loli.net/2020/06/30/zqhwLifIoa5xk24.png)

## new_autoreport.py的使用方法

![image-20210119164721455](https://i.loli.net/2021/01/19/MhaBDz2tHjmZyAg.png)

在此处添加上面抓包的内容即可，名字就填自己的。

### 4.填写经纬度，为防止意外

这个可以使用高德地图官网的工具，自己谷歌吧！

![image-20200630143742287](https://i.loli.net/2020/06/30/iPqdop2h5XlnmD8.png)

### 5.填写所在地信息，也就是平时的定位

填写的内容有`province`（省），`city`（市），`district`（区或县）等，关于这些的都填了吧！可以按照手机定位的信息填写。

![image-20200630143442693](https://i.loli.net/2020/06/30/HenRqMhdow8sryQ.png)

# 每天定时自动上报

## Windows下：创建任务计划程序

**先说结果，创建后等了两天，发现计算机关机后好像程序并不会定时执行。如果能保证计算机每天都开机可以使用，运行时间就自行设定。**

参考文章：https://blog.csdn.net/u012849872/article/details/82719372

![image-20200630144238889](https://i.loli.net/2020/06/30/rGiaeJXZzLAKTfy.png)

## Linux下，使用`crontab`创建定时任务：

**和Windows下一样，虚拟机关机后也不会运行，具体步骤可以参考下面，方法一样，就是一个是服务器，一个是本地的**，能保证每天运行Linux环境也可以使用这种方法。

# 最后，部署到云服务器上（可行）

### 1. 安装anaconda环境，或者python环境

### 2. 使用Linux下`crontab`命令创建定时计划任务：

经过测试，发现创建的`crontab`计划任务必须要在**系统级**，否则在XSehll或ssh连接关闭后，定时任务并不会运行。

1. 运行命令`vim /etc/crontab`

2. 在文件中添加下面命令

   `0 7 * * * root /root/anaconda3/bin/python /root/MyCode/AutoReport/autoreport.py >/dev/null 2>&1`

   推荐使用绝对路径，避免`python`环境找不到，当然也可以自己设置环境变量，系统级任务要指定用户名。

下面是关于`crontab`的使用介绍：

![image-20200630100546204](https://i.loli.net/2020/06/30/yRuJ5q2Graw4z9s.png)

https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html

