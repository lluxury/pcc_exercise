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
]
