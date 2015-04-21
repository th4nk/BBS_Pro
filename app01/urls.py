from django.conf.urls import patterns, include, url
from django.contrib import admin
#import models
from app01 import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^detail/(\d+)/$',views.bbs_detail),
                       url(r'^sub_comment/$',views.sub_comment),
                       url(r'^bbs_sub/$',views.bbs_sub),
                       url(r'^bbs_pub/$', views.bbs_pub),
                       url(r'^category/(\d+)/$',views.category)
                       
                       
)
