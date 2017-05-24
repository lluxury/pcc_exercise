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

#要后台运行么,每次进入bash都要开启环境? 确认

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


#管理网站
python manage.py createsuperuser
cd learning_logs
vi admin.py


#定义模型Entry
vi models.py

#python manage.py makemigrations app_name
python manage.py makemigrations learning_logs
python manage.py migrate
#注册模型
vi admin.py

#django shell
source ll_env/bin/activate
python manage.py shell

from learning_logs.models import Topic
Topic.objects.all()

topics = Topic.objects.all()
for topic in topics:
	print(topic.id, topic)

t = Topic.objects.get(id=1)
t.text
t.date_added

t.entry_set.all()




#创建网页
#流程 定义URL、编写视图和编写模板, 每个url都有映射视图,视图通常调用一个模板
vi learning_log/urls.py
vi learning_logs/urls.py
vi learning_logs/views.py 

cd /var/learning_log/learning_logs/
mkdir template
cd template/
mkdir learning_logs
cd learning_logs/
touch index.html
vi index.html

#模板
cd learning_logs/templates/learning_logs/
vi base.html
index.html

#占狗
#主题页及详情页
vi learning_logs/urls.py
vi learning_logs/views.py 
cd learning_logs/templates/learning_logs/
vi topics.html
vi base.html 

vi learning_logs/urls.py
# /(?P<topic_id>\d+)/ 匹配两个斜杠中的整数,并存在topic_id中

vi learning_logs/views.py
touch learning_logs/templates/learning_logs/topic.html
vi learning_logs/templates/learning_log/topic.html
#<a herf="{% url 'learning_logs:topic' topic.id %}"">{{ topic }}</a>
#一个小错误耽误1小时,还不报错,虽然开头就看了,但还是看的不仔细orz

vi learning_logs/templates/learning_log/topics.html

https://docs.djangoproject.com/en/1.11/ref/templates/


#用户添加主题
cd learning_logs/
vi forms.py
vi urls.py 
vi views.py 
cd templates/learning_logs/
vi new_topic.html
vi topics.html 

#需要通过管理页面操作,限制未知,教程不用,后面复习时排查
#用户添加文章
cd learning_logs/
vi forms.py 
vi urls.py 
vi views.py 
#widgets 小部件,表单元素
cd templates/learning_logs/
vi new_entry.html
vi /var/learning_log/learning_logs/views.py
vi /var/learning_logs/templates/learning_logs/topic.html

#还有一个疑问, 为什么走admin就不报错了? admin走的是自己的方法

#编辑文章
cd learning_logs/
vi urls.py 
vi views.py 
vi templates/learning_logs/edit_entry.html
vi templates/learning_logs/topic.html 

#创建用户帐户
#分层设计 项目(app,app) 每个有自己的url和view等,递归控制
python manage.py startapp users
vi learning_log/settings.py 
vi learning_log/urls.py 
vi users/urls.py
mkdir -p users/templates/users
vi users/templates/users/login.html
vi learning_logs/templates/learning_logs/base.html
#注销
vi users/urls.py 
vi users/views.py 
vi learning_logs/templates/learning_logs/base.html 
