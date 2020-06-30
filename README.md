# AutoReport

北京化工大学疫情上报

# 使用方法：

- 打开企业微信，打开Fiddle，进行抓包，具体过程看源仓库介绍
- 在指定位置填写cookies
- 填写经纬度，为防止意外，还需要填写所在省份等信息
- 可根据代码注释自己填写，目前要修改的就上面几个内容

# 每天定时自动上报

## Linux下，下面是在腾讯云服务器上的示例：

### 1. 安装anaconda环境，或者python环境

### 2. 使用Linux下`crontab`命令创建定时计划任务：

经过测试，发现创建的`crontab`计划任务必须要在系统级，否则在XSehll关闭后，定时任务并不会运行。

1. 运行命令`vim /etc/crontab`

2. 在文件中添加下面命令

   `* 7 * * * root /root/anaconda3/bin/python /root/MyCode/AutoReport/autoreport.py >/dev/null 2>&1`

   推荐使用绝对路径，避免`python`环境找不到，当然也可以自己设置环境变量，系统级任务要指定用户名。

下面是关于`crontab`的使用介绍：

![image-20200630100546204](https://i.loli.net/2020/06/30/yRuJ5q2Graw4z9s.png)

https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html

# 参考来自：

https://github.com/W0n9/BUCT_nCoV_Report

