from django.http import HttpResponse
from django.shortcuts import render


def DispalyHist(request):
    #判断username是否存在session中
    if "username" in request.session:
        user=request.session['username']
        print user
        if user:
            return render(request,'HistoryData.html', {'user': user})
    else:
        return render(request,'HistoryData.html', {'user': None})

def DispalyNow(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render(request,'NowData.html', {'user': user})
    else:
        return render(request,'NowData.html', {'user': None})

def DisRecord(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render(request,'Record.html', {'user': user})
    else:
        return render(request,'Record.html', {'user': None})

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
            return render(request, 'ChangeData.html', {'user': user})
    else:
        return render(request, 'ChangeData.html', {'user': None})