# coding=utf-8
'''
@author: ElegyPrince
'''
import  MySQLdb
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
