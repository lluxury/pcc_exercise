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
django-admin.py startproject learning_log .

python manage.py migrate

python manage.py runserver
#curl 127.0.0.1:8000|grep worked



