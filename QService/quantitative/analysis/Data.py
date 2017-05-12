# coding=utf-8
'''
Created on 2016-10-26
@author: Jennifer
Project:读取mysql数据库的数据，转为json格式
'''
import  MySQLdb

def Data(id_plan):
    try:
        # 1-7：如何使用python DB API访问数据库流程的
        # 1.创建mysql数据库连接对象connection
        # connection对象支持的方法有cursor(),commit(),rollback(),close()
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        # 2.创建mysql数据库游标对象 cursor
        # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
        cur = conn.cursor()
        # 3.编写sql
        sql = "SELECT alInvest,volume,alterms FROM valueplan where id = %s"
        # 4.执行sql命令
        # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
        cur.execute(sql,(id_plan))
        # 5.获取数据
        # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
        # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
        data = cur.fetchall()
        print u'fetchall()返回的数据：', data
        # 6.关闭cursor
        cur.close()
        # 7.关闭connection
        conn.close()
    except:
        print 'DA MySQL connect fail...'
    else:
        return data


def change_over(id_plan):
    m=0
    try:
        # 1-7：如何使用python DB API访问数据库流程的
        # 1.创建mysql数据库连接对象connection
        # connection对象支持的方法有cursor(),commit(),rollback(),close()
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        # 2.创建mysql数据库游标对象 cursor
        # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
        cur = conn.cursor()
        # 3.编写sql
        sql = "update valueplan set over=0 where id = %s"
        m=cur.execute(sql,(id_plan))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print 'DA MySQL connect fail...'
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
