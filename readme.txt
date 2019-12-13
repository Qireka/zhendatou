author: Wangzhepeng/qireka
server: Aliyun
ip: 116.62.15.17
domain name: www.zhendatou.cn

用的阿里云的学生机，1核2G  1M带宽   50G硬盘
阿里云很难受的一点是有个安全组，要用哪个端口就要去安全组设置一下，相当于防火墙
系统用镜像市场里装好了的centos7，自带python3.7，django模块，mysql
自己装nginx和uwsgi，暂时不考虑apache

代码时跟着某B站up一步一步写（抄）的，改了一些不重要的东西：

直至该博客发布（可能后面也不会更新了），完成的功能大概有：
写博客， 引用的ckeidtor表单， 评论和回复，查看评论数和阅读数，注册登录，修改昵称，绑定邮箱
写博客暂时只有我写，在后端/admin，如有人有写博客需要可以考虑放到前台

nginx：
配置文件在/etc/nginx/sites-available/zhendatou.conf  ---> /etc/nginx/conf.d
centos7的nginx跟之前用的ubuntu的目录结构不太一样，没有ubuntu的sites-available（可用的）和sites-enable（使用中的）这两个配置文件夹，只有一个conf.d
所以直接放进conf.d就行，或者自己创一个available搞个软连接到conf.d,这里需要把nginx.conf中的server配置注释掉，否则不会生效

uwsgi：
咋配置没记住，视频看，配置文件在/home/zhendatou_uwsgi/zhendatou.ini



友情链接：
B站_再敲一行代码:https://space.bilibili.com/252028233/channel/detail?cid=28138
bootstrap:https://www.bootcss.com/
ckeditor:https://ckeditor.com/docs/ckeditor5/latest/



