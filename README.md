pyWebpj
=======

主要是一个web.py apache wsgi 工程
主要目的：学习python


#工作环境
     
     *后台
     Python: 2.7.8
     apache:2.2
     IDEA:pyCharm3.4(http://www.jetbrains.com/pycharm/)
     test：nose、nose-cov1.6（https://pypi.python.org/pypi/nose-cov/）
     Web：web.py（http://webpy.org/static/web.py-0.37.tar.gz）
     db: MYSQLDb(http://sourceforge.net/projects/mysql-python/)
     *前台
     angularjs-1.2.9
     bootstrap
     html5

#apache配置

    加载mod_wsgi.so 模块
    在http.conf；
    LoadModule wsgi_module modules/mod_wsgi.so //加载mod_wsgi.so 模块
    //#Ensure that Apache listens on port 80
    Listen 8080//端口监听，可自定义
    //#Listen for virtual host requests on all IP addresses
    NameVirtualHost *:8080
    <VirtualHost *:8080>
    DocumentRoot "/pyWebpj" //python 工程目录
    ServerName www.python.com
    //#mounts your application if mod_wsgi is being used
    WSGIScriptAlias /python  "/pyWebpj/code.py"
    //#the Alias directive
    Alias /python/static "/static" //静态文件目录
    <Directory />
        Order Allow,Deny
        Allow From All
        Options -Indexes
    </Directory>
    //# because Alias can be used to reference resources outside docroot, you
    //# must reference the directory with an absolute path
    <Directory "/static">
        # directives to effect the static directory
        Options +Indexes
    </Directory>
    </VirtualHost> 
    
#参数配置

     参数文件路劲：/config/config.json;   具体请看：config/参赛说明.html
     
#试一试

     打开浏览器，输入http://127.0.0.1:8080/python/
     *如果看到结果：this is a python web 则表示成功

