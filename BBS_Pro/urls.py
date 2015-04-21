from django.conf.urls import patterns, include, url
from django.contrib import admin
import app01.urls
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include(app01.urls)),
    url(r'^accounts/login/$','django.contrib.auth.views.login'),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout_view),
    url(r'^acc_login/$',views.acc_login),
    url(r'^register/$', views.register),
)
