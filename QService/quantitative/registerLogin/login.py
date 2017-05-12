#coding=utf-8
from django.http import HttpResponse
import quantitative.secret.MD5 as MD
import MySQLdb
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def post_login(request):
    if request.POST:
        try:
            psd = request.POST['Fpsd']
            phone = request.POST['Fphone']
            conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
            cur = conn.cursor()
            sql = "select * from user where password = %s and phone = %s limit 1"
            cur.execute(sql,(MD.md5(psd),MD.md5(phone)))
            data = cur.fetchall()
            print u'data值',data
            cur.close()
            conn.close()
        except:
            print 'MySQL connect fail...'
        else:
            #没有查询到数据，登录错误
            if data==():
                return HttpResponse('false')
            else:
                # 将username,userid写入浏览器session
                request.session['username']=data[0][3]
                request.session['userid'] = data[0][4]
                return HttpResponse('true')
    else:
        print "未获取到数据"


def logout(request):
    print "登出",request.session['username']
    print "登出",request.session['userid']
    if "username" in request.session:
        del request.session['username']
        if "userid" in request.session:
            del request.session['userid']
        return HttpResponse("delete")
    else:
        return HttpResponse("false")