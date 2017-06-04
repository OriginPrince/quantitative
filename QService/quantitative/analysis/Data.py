# coding=utf-8
'''
@author: ElegyPrince
@project:从数据库中获取数据
'''
import  MySQLdb
import tushare as ts
import random
#查询id_plan的数据
def Data(id_plan):
    try:
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = "SELECT alInvest,volume,alterms FROM valueplan where id = %s"
        cur.execute(sql,(id_plan))
        data = cur.fetchall()
        print u'查询id_plan返回的数据：', data
        cur.close()
        conn.close()
    except:
        print '查询id_plan的数据 MySQL connect fail...'
    else:
        return data

#修改id_plan数据的over为0
def change_over(id_plan):
    m=0
    try:
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = "update valueplan set over=0 where id = %s"
        m=cur.execute(sql,(id_plan))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print '修改id_plan数据的over为0 MySQL connect fail...'
    else:
        return m

#检查id_plan是否已经结束，over字段是否为0
def Data_over(id_plan):
    try:
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = "SELECT over FROM valueplan where id = %s"
        cur.execute(sql,(id_plan))
        data = cur.fetchall()
        print u'检查id_plan是否已经结束返回的数据：', data
        cur.close()
        conn.close()
    except:
        print '检查id_plan是否已经结束 MySQL connect fail...'
    else:
        return data

#计算id_plan的收益率
def Data_rateReturn(id_plan,stock_id):
    m=0
    try:
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        cur = conn.cursor()
        sql = "SELECT alInvest,volume FROM valueplan where id = %s"
        cur.execute(sql,(id_plan))
        data = cur.fetchall()
        print u'data的值', data
        alInvest=data[0][0]
        volume=data[0][1]
        print alInvest,volume
        fd = ts.get_realtime_quotes(stock_id)
        price = float(fd['price'])  # 每股的价格
        #price = random.uniform(0.9, 1.2)  # 模拟计算的
        alValue=price*volume
        returnRate=(alValue-alInvest)/alInvest
        print "股指收益率",returnRate
        sql = "update valueplan set rateReturn=%s where id = %s"
        m = cur.execute(sql, (returnRate,id_plan))
        conn.commit()
        cur.close()
        conn.close()
        print m

    except:
        print '检查id_plan是否已经结束 MySQL connect fail...'
    else:
        return m