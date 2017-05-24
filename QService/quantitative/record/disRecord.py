# coding=utf-8
'''
@author: ElegyPrincess
'''
import  MySQLdb
import quantitative.bean.changeFinal as CF
import quantitative.bean.changeInitinal as CI
import quantitative.bean.changeAlFinal as AF
import quantitative.bean.record as RE
from django.shortcuts import render

def recordList(request):
    if "username" in request.session:
        user = request.session['username']
        id_user = request.session['userid']  # 用户id
        #id_user=4
        try:
            # 1-7：如何使用python DB API访问数据库流程的
            # 1.创建mysql数据库连接对象connection
            # connection对象支持的方法有cursor(),commit(),rollback(),close()
            conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
            # 2.创建mysql数据库游标对象 cursor
            # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
            cur = conn.cursor()
            # 3.编写sql
            # sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
            sql = "SELECT id,time,ultimateInvest,over,rateReturn,terms,rateInvest,rateTax,dayCount  FROM valueplan where id_user=%s and class=1"
            # 4.执行sql命令
            # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
            cur.execute(sql, (id_user))
            # 5.获取数据
            # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
            # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
            data = cur.fetchall()
            CFList=[]
            for d in data:
                print u'数据：', d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8]
                CF1=CF.changeFinal(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8])
                CFList.append(CF1)

            # 3.编写sql
            # sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
            sql1 = "SELECT id,time,initiateInvest,over,rateReturn,terms,rateInvest,rateTax,dayCount  FROM valueplan where id_user=%s and class=0"
            # 4.执行sql命令
            # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
            cur.execute(sql1, (id_user))
            # 5.获取数据
            # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
            # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
            data1 = cur.fetchall()
            CIList=[]
            for d in data1:
                print u'数据：', d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7]
                CI1=CI.changeInitinal(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8])
                CIList.append(CI1)


            # 3.编写sql
            # sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
            sql2= "SELECT id,IVInvest,time,initiateInvest,over,rateReturn,terms,rateInvest,rateTax,dayCount  FROM valueplan where id_user=%s and class=0"
            # 4.执行sql命令
            # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
            cur.execute(sql2, (id_user))
            # 5.获取数据
            # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
            # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
            data2 = cur.fetchall()
            AFList=[]
            for d in data2:
                print u'数据：', d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8]
                AF1=AF.changeAlFinal(d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9])
                AFList.append(AF1)

            # 6.关闭cursor
            cur.close()
            # 7.关闭connection
            conn.close()
        except:
            print 'MySQL connect fail...'
        else:
            return render(request, 'record/recordList.html', {'CF': CFList, 'CI':CIList, 'AF':AFList, 'user': user})
    else:
        return render(request, 'record/recordList.html', {'CF': None, 'CI': None, 'AF': None, 'user': None})

def recordDetail(request):
    if "username" in request.session:
        user = request.session['username']
        if request.GET:
            id_plan = request.GET['id_plan']
            try:
                # 1-7：如何使用python DB API访问数据库流程的
                # 1.创建mysql数据库连接对象connection
                # connection对象支持的方法有cursor(),commit(),rollback(),close()
                conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306,
                                       charset='utf8')
                # 2.创建mysql数据库游标对象 cursor
                # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
                cur = conn.cursor()
                # 3.编写sql
                # sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
                sql = "SELECT date,term,invest,stock  FROM record where id_plan=%s "
                # 4.执行sql命令
                # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
                cur.execute(sql, (id_plan))
                # 5.获取数据
                # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
                # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
                data = cur.fetchall()
                REList = []
                for d in data:
                    print u'数据：', d[0], d[1], d[2], d[3]
                    RE1 = RE.record(d[0], d[1], d[2], d[3])
                    REList.append(RE1)
                # 6.关闭cursor
                cur.close()
                # 7.关闭connection
                conn.close()
                return render(request, 'record/recordDetail.html', {'Detail': REList, 'user': user})
            except:
                print 'MySQL connect fail...'

        else:
            return render(request, 'record/recordDetail.html', {'Detail': None, 'user': None})
    else:
        return render(request, 'record/recordDetail.html', {'Detail': None, 'user': None})

