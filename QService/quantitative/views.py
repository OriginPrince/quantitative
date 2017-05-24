#coding=utf-8
from django.shortcuts import render


def DispalyHist(request):
    #判断username是否存在session中
    if "username" in request.session:
        user=request.session['username']
        print user
        if user:
            return render(request, 'disHist/HistoryData.html', {'user': user})
    else:
        return render(request, 'disHist/HistoryData.html', {'user': None})

def DispalyNow(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render(request, 'disNow/NowData.html', {'user': user})
    else:
        return render(request, 'disNow/NowData.html', {'user': None})


def register(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render(request,'register.html', {'user': user})
    else:
        return render(request,'register.html', {'user': None})

def change(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render(request, 'change/ChangeData.html', {'user': user})
    else:
        return render(request, 'change/ChangeData.html', {'user': None})
