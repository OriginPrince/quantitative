# coding=utf-8
import tushare as ts
import MySQLdb
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import create_engine


timenow = time.strftime("%Y-%m-%d", time.localtime())
engine=create_engine('mysql://root:888212@127.0.0.1/economic?charset=utf8')


# 1-7：如何使用python DB API访问数据库流程的
# 1.创建mysql数据库连接对象connection
# connection对象支持的方法有cursor(),commit(),rollback(),close()
conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
# 2.创建mysql数据库游标对象 cursor
# cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
cur = conn.cursor()
# 3.编写sql
#sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
sql_sh = "select * from sh_hist_data order by date desc limit 1"
sql_sz = "select * from sz_hist_data order by date desc limit 1"
sql_sz50 = "select * from sz50_hist_data order by date desc limit 1"
sql_hs300 = "select * from hs300_hist_data order by date desc limit 1"
sql_zxb = "select * from zxb_hist_data order by date desc limit 1"
sql_cyb = "select * from cyb_hist_data order by date desc limit 1"
# 4.执行sql命令
# execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
cur.execute(sql_sh)
# 5.获取数据
# fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
# 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
sh_result= cur.fetchall()

cur.execute(sql_sz)
sz_result= cur.fetchall()

cur.execute(sql_sz50)
sz50_result= cur.fetchall()

cur.execute(sql_hs300)
hs300_result= cur.fetchall()

cur.execute(sql_zxb)
zxb_result= cur.fetchall()

cur.execute(sql_cyb)
cyb_result= cur.fetchall()

'''date maybe unlikeness'''
def sh_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = sh_result[0][0]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        sh_df = ts.get_h_data('000001', index=True, start=timeold, end=timenow)
        if sh_df is not None:
            sh_df.to_sql('sh_hist_data', engine, if_exists='append')
            print "insert successfully"


def sz_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = sz_result[0][0]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        sz_df = ts.get_h_data('399001', index=True, start=timeold, end=timenow)
        if sz_df is not None:
            sz_df.to_sql('sz_hist_data', engine, if_exists='append')
            print "insert successfully"


def hs300_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = hs300_result[0][0]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        hs300_df = ts.get_h_data('000300', index=True, start=timeold, end=timenow)
        if hs300_df is not None:
            hs300_df.to_sql('hs300_hist_data', engine, if_exists='append')
            print "insert successfully"


def sz50_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = sz50_result[0][0]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        sz50_df = ts.get_h_data('000016', index=True, start=timeold, end=timenow)
        if sz50_df is not None:
            sz50_df.to_sql('sz50_hist_data', engine, if_exists='append')
            print "insert successfully"


def zxb_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = zxb_result[0][0]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        zxb_df = ts.get_h_data('399005', index=True, start=timeold, end=timenow)
        if zxb_df is not None:
            zxb_df.to_sql('zxb_hist_data', engine, if_exists='append')
            print "insert successfully"


def cyb_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = cyb_result[0][0]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        cyb_df = ts.get_h_data('399006', index=True, start=timeold, end=timenow)
        if cyb_df is not None:
            cyb_df.to_sql('cyb_hist_data', engine, if_exists='append')
            print "insert successfully"

if sh_result==():
    sh_df = ts.get_h_data('000001', index=True, start='1995-01-01', end=timenow)
    sh_df.to_sql('sh_hist_data', engine, if_exists='append')
    print "insert successfully"
else:
    sh_job()
	
if sz_result==():
    sz_df = ts.get_h_data('399001', index=True, start='1995-01-01', end=timenow)
    sz_df.to_sql('sz_hist_data', engine, if_exists='append')
    print "insert successfully"
else:
    sz_job()
	
if hs300_result==():
    hs300_df = ts.get_h_data('000300', index=True, start='2005-04-08', end=timenow)
    hs300_df.to_sql('hs300_hist_data', engine, if_exists='append')
    print "insert successfully"
else:
    hs300_job()
	
if sz50_result==():
    sz50_df = ts.get_h_data('000016', index=True, start='2004-01-01', end=timenow)
    sz50_df.to_sql('sz50_hist_data', engine, if_exists='append')
    print "insert successfully"
else:
    sz50_job()
	
if zxb_result==():
    zxb_df = ts.get_h_data('399005', index=True, start='2008-06-30', end=timenow)
    zxb_df.to_sql('zxb_hist_data', engine, if_exists='append')
    print "insert successfully"
else:
    zxb_job()
	
if cyb_result==():
    cyb_df = ts.get_h_data('399006', index=True, start='2010-06-01', end=timenow)
    cyb_df.to_sql('cyb_hist_data', engine, if_exists='append')
    print "insert successfully"
else:
    cyb_job()



def job():
    sh_job()
    sz_job()
    hs300_job()
    sz50_job()
    zxb_job()
    cyb_job()


if __name__=='__main__':

	scheduler = BackgroundScheduler()
	scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour=19, minute=35)
	scheduler.start()
	try:
		while True:
			time.sleep(2)
	except (KeyboardInterrupt,SystemExit):
		scheduler.shutdown()
