#coding=utf-8
'''
@author: ElegyPrincess
project:中间件来对url进行拦截
'''
from django.conf import settings
from re import compile
from django.shortcuts import render_to_response
from django.utils.deprecation import MiddlewareMixin

#将要转化的url转化成正则表达式格式的列表
if hasattr(settings,'EXEMPT_URLS'):
    exemptUrls = [compile(expr) for expr in settings.EXEMPT_URLS]

#进行正则表达式的匹配，如果是想要拦截的url，将页面跳转到历史数据页面
class LoginRequireMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'username' not in  request.session:
            path=request.path.lstrip('/')
            flag=0
            for m in exemptUrls:
                result=m.search(path)
                if result is not None:
                    flag=1
            if flag==1:
                return render_to_response('disHist/HistoryData.html')
