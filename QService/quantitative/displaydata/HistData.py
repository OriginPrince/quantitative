# coding=utf-8
'''
@author: ElegyPrincess
'''
import  MySQLdb


def histPrice(date,stock):
        try:
            # 1-7：如何使用python DB API访问数据库流程的
            # 1.创建mysql数据库连接对象connection
            # connection对象支持的方法有cursor(),commit(),rollback(),close()
            conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
            # 2.创建mysql数据库游标对象 cursor
            # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
            cur = conn.cursor()
            # 3.编写sql
            #sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
            sql = "SELECT date,open,close,low,high,volume,amount FROM "+stock+" where date=%s"
            # 4.执行sql命令
            # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
            cur.execute(sql,(date))
            # 5.获取数据
            # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
            # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
            data = cur.fetchall()
            print u'数据：', data
            # 6.关闭cursor
            cur.close()
            # 7.关闭connection
            conn.close()
        except:
            print stock+'MySQL connect fail...'
        else:
            return data

def histData(stock):
    try:
        # 1-7：如何使用python DB API访问数据库流程的
        # 1.创建mysql数据库连接对象connection
        # connection对象支持的方法有cursor(),commit(),rollback(),close()
        conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
        # 2.创建mysql数据库游标对象 cursor
        # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
        cur = conn.cursor()
        # 3.编写sql
        sql = "SELECT date,open,close,low,high,volume,amount FROM "+stock
        print sql
        # 4.执行sql命令
        # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
        cur.execute(sql)
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
        print stock+'price MySQL connect fail...'
    else:
        return data

