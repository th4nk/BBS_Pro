#coding:utf8
from django.contrib import admin
from app01 import models
# Register your models here.



class BBS_admin(admin.ModelAdmin):
    list_display = ('title','author','photo','signature','summary','view_count')
    list_filter = ('created_at',)
    search_fields = ('author__user__username','title')

    def signature(self,ob):
        return ob.author.signature

    def photo(self,obj):
        return obj.author.photo

    #title.short_description = u'标题'
    #author.short_description = u'作者'
    signature.short_description = u'签名'
    #summary.short_description = u'摘要'

admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
