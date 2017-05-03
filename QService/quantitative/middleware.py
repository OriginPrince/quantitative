#coding=utf-8
from django.conf import settings
from re import compile
from django.shortcuts import render_to_response
from django.utils.deprecation import MiddlewareMixin

if hasattr(settings,'EXEMPT_URLS'):
    exemptUrls = [compile(expr) for expr in settings.EXEMPT_URLS]

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
                return render_to_response('HistoryData.html')
