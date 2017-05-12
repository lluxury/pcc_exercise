#Django
yum install sqlite-devel
#要要venv前安装,不然sqlite会报错

python3 -m venv ll_env
#若失败
#pip3 install --user virtualenv
#sudo apt-get install python-virtualen

cd /var/learning_log
#应用根目录

#virtualenv ll_env
/root/.local/bin/virtualenv ll_env --python=python3

source ll_env/bin/activate
#激活 注意 /var/learning_log

deactivate
#停用

pip install Django
#Django-1.11.1

#Django仅在虚拟环境处于活动状态时才可用
#一开始就应该上传所有文档,除了虚拟环境

django-admin.py startproject learning_log .

python manage.py migrate

python manage.py runserver
#curl 127.0.0.1:8000|grep worked

#要后台运行么,每次进入bash都要开启环境?

python manage.py startapp learning_logs

cd learning_logs/
vi models.py 
#https://docs.djangoproject.com/en/1.11/ref/models/fields/

cd learning_log/
vi settings.py

python manage.py makemigrations learning_logs
#生成修改方法

python manage.py migrate
#更新数据库
#每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤：修改models.py；对learning_logs 调用makemigrations；让Django迁移项目


