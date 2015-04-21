#coding:utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import models
from django.template.context import RequestContext
from django.contrib import auth,comments
from models import UserFile
from django import forms
# Create your views here.


def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        content = '''
        Welcome %s !!!
        
        <a href='/logout/' >Logout</a>
        
         ''' % user.username
        #return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
    

def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/index/'>Re-login</a>" % user)


def login(request):
    return render_to_response('login.html')



def index(request):
    
    bbs_list = models.BBS.objects.all()
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html', {
                                             'bbs_list':bbs_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})



def category(request,cata_id):
    bbs_list = models.BBS.objects.filter(category__id=cata_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',
                               {'bbs_list':bbs_list,
                                 'user':request.user,
                                 'bbs_category':bbs_categories,
                                 'cata_id': int(cata_id),
                              })



def bbs_detail(request, bbs_id):
    bbs_categories = models.Category.objects.all()
    bbs = models.BBS.objects.get(id=bbs_id)
    print '--->', bbs
   
    return render_to_response('bbs_detail.html', {'bbs_obj':bbs,'user':request.user,'bbs_category':bbs_categories,})
    
def sub_comment(request):
    print  request.POST
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')    
    
    comments.models.Comment.objects.create(
            content_type_id = 7,
            object_pk= bbs_id,
            site_id = 1,
            user = request.user,                       
            comment =   comment,                   
                                   )
    return  HttpResponseRedirect('/detail/%s' % bbs_id) 

def bbs_pub(request):
    return render_to_response('bbs_pub.html') 


def bbs_sub(request):
    print ',==>', request.POST.get('content')
    content =  request.POST.get('content')
    author = models.BBS_user.objects.get(user__username=request.user)
    title =  request.POST.get('title')
    summary =  request.POST.get('summary')
    category = request.POST.get('category')
    models.BBS.objects.create(
        title = title,
        summary = summary,
        content = content,
        author =author,
        view_count= 1,
        ranking = 1,
        category_id = category
           )

    return HttpResponseRedirect("/")
class UserForm(forms.Form):
    username = forms.CharField(label=u'用户名',max_length=100)
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput())
    email = forms.EmailField(label=u'邮箱')
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']

            user = UserFile()
            user.username = username
            user.password = password
            user.email = email
            user.save()

            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()

    return render_to_response('register.html',{'uf':uf})
            
