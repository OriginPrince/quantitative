#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
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
            # 1-7：如何使用python DB API访问数据库流程的
            # 1.创建mysql数据库连接对象connection
            # connection对象支持的方法有cursor(),commit(),rollback(),close()
            conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306,
                                   charset='utf8')
            # 2.创建mysql数据库游标对象 cursor
            # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
            cur = conn.cursor()
            # 3.编写sql
            sql1 = "select * from user where phone=%s"
            # 4.执行sql命令
            # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
            cur.execute(sql1, (MD.md5(phone)))
            num = cur.fetchall()
            n=0
            if num==():
                sql2 = "insert into user (name,password,phone,email) values (%s,%s,%s,%s)"
                # 4.执行sql命令
                # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
                n=cur.execute(sql2, (name, MD.md5(psd), MD.md5(phone), MD.md5(email)))
                conn.commit()
            #print "data"+data
            # 5.获取数据
            # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
            # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
            #data = cur.fetchall()
            #print u'登录结果：', data
            # 6.关闭cursor
            sql3 = "select id from user where phone=%s"
            # 4.执行sql命令
            # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
            cur.execute(sql3, (MD.md5(phone)))
            id = cur.fetchall()
            print "id",id
            cur.close()
            # 7.关闭connection
            conn.close()
        except:
            print 'MySQL connect fail...'
            return HttpResponse('error')
        else:
            # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
            # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
            # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
            if num is not ():
                return HttpResponse("already")
            elif n==1:
                request.session['username'] =name
                request.session['userid']=id[0][0]
                return HttpResponse("true")
            else:
                return HttpResponse("false")
    else:
        print "未获取到数据"
