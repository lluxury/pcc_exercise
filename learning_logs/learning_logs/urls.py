"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),
    
    #显示所有主题
    url(r'^topics/$', views.topics, name='topics'),

    # 详情页
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #url(r'^topics/(?P<topic_id\d+>)/$', views.topic, name='topic'),
    
    #添加新主题
    #url(r'^new_topic/$, views.new_topic, name='new_topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #添加文章
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
