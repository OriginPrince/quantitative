#coding=utf-8
from django.http import HttpResponse
import quantitative.secret.MD5 as MD
from django.views.decorators.csrf import csrf_exempt
import MySQLdb

@csrf_exempt
def post_register(request):
    if request.POST:
        try:
            name = request.POST['Fname']
            psd = request.POST['Fpsd']
            phone = request.POST['Fphone']
            email = request.POST['Femail']
            print name+psd+phone+email
            conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306,
                                   charset='utf8')
            cur = conn.cursor()
            # 3.编写sql
            sql1 = "select * from user where phone=%s"
            cur.execute(sql1, (MD.md5(phone)))
            num = cur.fetchall()
            n=0
            if num==():
                sql2 = "insert into user (name,password,phone,email) values (%s,%s,%s,%s)"
                #如果执行成功，返回值为1，失败返回值为0
                n=cur.execute(sql2, (name, MD.md5(psd), MD.md5(phone), MD.md5(email)))
                #注意数据库事务需要提交
                conn.commit()
            sql3 = "select id from user where phone=%s"
            cur.execute(sql3, (MD.md5(phone)))
            id = cur.fetchall()
            print "id",id
            cur.close()
            conn.close()
        except:
            print 'MySQL connect fail...'
            return HttpResponse('error')
        else:
            #手机号码已经存在
            if num is not ():
                return HttpResponse("already")
            #注册成功
            elif n==1:
                request.session['username'] =name
                request.session['userid']=id[0][0]
                return HttpResponse("true")
            #注册失败
            else:
                return HttpResponse("false")
    else:
        print "未获取到数据"
