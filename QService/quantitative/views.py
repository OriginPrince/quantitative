from django.shortcuts import render_to_response

def DispalyHist(request):
    if "username" in request.session:
        user=request.session['username']
        print user
        if user:
            return render_to_response('HistoryData.html', {'user': user})
    else:
        return render_to_response('HistoryData.html')

def DispalyNow(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render_to_response('NowData.html', {'user': user})
    else:
        return render_to_response('NowData.html')

def DisRecord(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render_to_response('Record.html', {'user': user})
    else:
        return render_to_response('Record.html')

def register(request):
    if "username" in request.session:
        user = request.session['username']
        print user
        if user:
            return render_to_response('register.html', {'user': user})
    else:
        return render_to_response('register.html')
