# coding=utf-8
import tushare as ts
import MySQLdb
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import create_engine


timenow = time.strftime("%Y-%m-%d", time.localtime())
engine=create_engine('mysql://root:888212@127.0.0.1/economic?charset=utf8')


conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
cur = conn.cursor()
sql_sh = "select * from histdata where stock='sh' order by date desc limit 1"
sql_sz = "select * from histdata where stock='sz' order by date desc limit 1"
sql_sz50 = "select * from histdata where stock='sz50' order by date desc limit 1"
sql_hs300 = "select * from histdata where stock='hs300' order by date desc limit 1"
sql_zxb = "select * from histdata where stock='zxb' order by date desc limit 1"
sql_cyb = "select * from histdata where stock='cyb' order by date desc limit 1"
#数据库中是否有数据
cur.execute(sql_sh)
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

#获取从数据库中的最新日期开始，到现在的数据
def sh_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = sh_result[0][1]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        sh_df = ts.get_h_data('000001', index=True, start=timeold, end=timenow)
        if sh_df is not None:
            sh_df['stock']='sh'
            sh_df.to_sql('histdata', engine, if_exists='append')
            print "insert successfully"


def sz_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = sz_result[0][1]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        sz_df = ts.get_h_data('399001', index=True, start=timeold, end=timenow)
        if sz_df is not None:
            sz_df['stock']='sz'
            sz_df.to_sql('histdata', engine, if_exists='append')
            print "insert successfully"


def hs300_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = hs300_result[0][1]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        hs300_df = ts.get_h_data('000300', index=True, start=timeold, end=timenow)
        if hs300_df is not None:
            hs300_df['stock']='hs300'
            hs300_df.to_sql('histdata', engine, if_exists='append')
            print "insert successfully"


def sz50_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = sz50_result[0][1]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        sz50_df = ts.get_h_data('000016', index=True, start=timeold, end=timenow)
        if sz50_df is not None:
            sz50_df['stock']='sz50'
            sz50_df.to_sql('histdata', engine, if_exists='append')
            print "insert successfully"


def zxb_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = zxb_result[0][1]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        zxb_df = ts.get_h_data('399005', index=True, start=timeold, end=timenow)
        if zxb_df is not None:
            zxb_df['stock']='zxb'
            zxb_df.to_sql('histdata', engine, if_exists='append')
            print "insert successfully"


def cyb_job():
    timenow = time.strftime("%Y-%m-%d", time.localtime())
    date = cyb_result[0][1]
    d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    delta = datetime.timedelta(days=1)
    tempttime = d + delta
    timeold = tempttime.strftime('%Y-%m-%d')
    if timenow > date:
        cyb_df = ts.get_h_data('399006', index=True, start=timeold, end=timenow)
        if cyb_df is not None:
            cyb_df['stock']='cyb'
            cyb_df.to_sql('histdata', engine, if_exists='append')
            print "insert successfully"

#如果数据库中没有数据，那么从头开始获取数据，否则的话从数据库最近日期开始获取到现在的数据
if sh_result==():
    sh_df = ts.get_h_data('000001', index=True, start='1995-01-01', end=timenow)
    sh_df['stock'] = 'sh'
    sh_df.to_sql('histdata', engine, if_exists='append')
    print "insert successfully"
else:
    sh_job()
	
if sz_result==():
    sz_df = ts.get_h_data('399001', index=True, start='1995-01-01', end=timenow)
    sz_df['stock'] = 'sz'
    sz_df.to_sql('histdata', engine, if_exists='append')
    print "insert successfully"
else:
    sz_job()
	
if hs300_result==():
    hs300_df = ts.get_h_data('000300', index=True, start='2005-04-08', end=timenow)
    hs300_df['stock'] = 'hs300'
    hs300_df.to_sql('histdata', engine, if_exists='append')
    print "insert successfully"
else:
    hs300_job()
	
if sz50_result==():
    sz50_df = ts.get_h_data('000016', index=True, start='2004-01-01', end=timenow)
    sz50_df['stock'] = 'sz50'
    sz50_df.to_sql('histdata', engine, if_exists='append')
    print "insert successfully"
else:
    sz50_job()
	
if zxb_result==():
    zxb_df = ts.get_h_data('399005', index=True, start='2008-06-30', end=timenow)
    zxb_df['stock'] = 'zxb'
    zxb_df.to_sql('histdata', engine, if_exists='append')
    print "insert successfully"
else:
    zxb_job()
	
if cyb_result==():
    cyb_df = ts.get_h_data('399006', index=True, start='2010-06-01', end=timenow)
    cyb_df['stock'] = 'cyb'
    cyb_df.to_sql('histdata', engine, if_exists='append')
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
    #制定定时任务
	scheduler = BackgroundScheduler()
	scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour=22, minute=00)
	scheduler.start()
	try:
		while True:
			time.sleep(2)
	except (KeyboardInterrupt,SystemExit):
		scheduler.shutdown()
