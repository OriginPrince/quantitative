# coding=utf-8
import tushare as ts
from sqlalchemy import create_engine
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler


timenow = time.strftime("%Y-%m-%d", time.localtime())
engine = create_engine('mysql://root:888212@127.0.0.1/economic?charset=utf8')
sh_result=engine.execute("select * from cyb_hist_data order by date desc limit 1")
sz_result=engine.execute("select * from cyb_hist_data order by date desc limit 1")
hs300_result=engine.execute("select * from cyb_hist_data order by date desc limit 1")
sz50_result=engine.execute("select * from cyb_hist_data order by date desc limit 1")
zxb_result=engine.execute("select * from cyb_hist_data order by date desc limit 1")
cyb_result=engine.execute("select * from cyb_hist_data order by date desc limit 1")

if sh_result is None:
    sh_df = ts.get_h_data('000001', index=True, start='1995-01-01', end=timenow)
    sh_df.to_sql('sh_hist_data', engine, if_exists='append')
    print "insert successfully"
if sz_result is None:
    sz_df = ts.get_h_data('399001', index=True, start='1995-01-01', end=timenow)
    sz_df.to_sql('sz_hist_data', engine, if_exists='append')
    print "insert successfully"
if hs300_result is None:
    hs300_df = ts.get_h_data('000300', index=True, start='2005-04-08', end=timenow)
    hs300_df.to_sql('hs300_hist_data', engine, if_exists='append')
    print "insert successfully"
if sz50_result is None:
    sz50_df = ts.get_h_data('000016', index=True, start='2004-01-01', end=timenow)
    sz50_df.to_sql('sz50_hist_data', engine, if_exists='append')
    print "insert successfully"
if sz50_result is None:
    zxb_df = ts.get_h_data('399005', index=True, start='2008-06-30', end=timenow)
    zxb_df.to_sql('zxb_hist_data', engine, if_exists='append')
    print "insert successfully"
if sz50_result is None:
    cyb_df = ts.get_h_data('399006', index=True, start='2010-06-01', end=timenow)
    cyb_df.to_sql('cyb_hist_data', engine, if_exists='append')
    print "insert successfully"

'''date maybe unlikeness'''
def sh_job():
    if sh_result is not None:
        timenow = time.strftime("%Y-%m-%d", time.localtime())
        a = sh_result.fetchall()
        sh_result.close()
        date = a[0][0]
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=1)
        tempttime = d + delta
        timeold = tempttime.strftime('%Y-%m-%d')
        if timenow > date:
            sh_df = ts.get_h_data('000001', index=True, start=timeold, end=timenow)
            if sh_df is not None:
                sh_df.to_sql('sh_hist_data', engine, if_exists='append')
		print "insert successfully"
    else:
        print 'sh error'
def sz_job():
    if sz_result is not None:
        timenow = time.strftime("%Y-%m-%d", time.localtime())
        a = sz_result.fetchall()
        sz_result.close()
        date = a[0][0]
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=1)
        tempttime = d + delta
        timeold = tempttime.strftime('%Y-%m-%d')
        if timenow > date:
            sz_df = ts.get_h_data('399001', index=True, start=timeold, end=timenow)
            if sz_df is not None:
                sz_df.to_sql('sz_hist_data', engine, if_exists='append')
		print "insert successfully"
    else:
        print 'sz error'
def hs300_job():
    if hs300_result is not None:
        timenow = time.strftime("%Y-%m-%d", time.localtime())
        a = hs300_result.fetchall()
        hs300_result.close()
        date = a[0][0]
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=1)
        tempttime = d + delta
        timeold = tempttime.strftime('%Y-%m-%d')
        if timenow > date:
            hs300_df = ts.get_h_data('000300', index=True, start=timeold, end=timenow)
            if hs300_df is not None:
                hs300_df.to_sql('hs300_hist_data', engine, if_exists='append')
		print "insert successfully"
    else:
        print 'hs300 error'
def sz50_job():
    if sz50_result is not None:
        timenow = time.strftime("%Y-%m-%d", time.localtime())
        a = sz50_result.fetchall()
        sz50_result.close()
        date = a[0][0]
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=1)
        tempttime = d + delta
        timeold = tempttime.strftime('%Y-%m-%d')
        if timenow > date:
            sz50_df = ts.get_h_data('000016', index=True, start=timeold, end=timenow)
            if sz50_df is not None:
                sz50_df.to_sql('sz50_hist_data', engine, if_exists='append')
		print "insert successfully"
    else:
        print 'sz50 error'
def zxb_job():
    if zxb_result is not None:
        timenow = time.strftime("%Y-%m-%d", time.localtime())
        a = zxb_result.fetchall()
        zxb_result.close()
        date = a[0][0]
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=1)
        tempttime = d + delta
        timeold = tempttime.strftime('%Y-%m-%d')
        if timenow > date:
            zxb_df = ts.get_h_data('399005', index=True, start=timeold, end=timenow)
            if zxb_df is not None:
                zxb_df.to_sql('zxb_hist_data', engine, if_exists='append')
		print "insert successfully"
    else:
        print 'zxb error'
def cyb_job():
    if cyb_result is not None:
        timenow = time.strftime("%Y-%m-%d", time.localtime())
        a = cyb_result.fetchall()
        cyb_result.close()
        date = a[0][0]
        d = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        delta = datetime.timedelta(days=1)
        tempttime = d + delta
        timeold = tempttime.strftime('%Y-%m-%d')
        if timenow > date:
            cyb_df = ts.get_h_data('399006', index=True, start=timeold, end=timenow)
            if cyb_df is not None:
                cyb_df.to_sql('cyb_hist_data', engine, if_exists='append')
		print "insert successfully"
    else:
        print 'cyb error'

def job():
    sh_job()
    sz_job()
    hs300_job()
    sz50_job()
    zxb_job()
    cyb_job()


if __name__=='__main__':
	scheduler = BackgroundScheduler()
	scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour=22, minute=00)
	scheduler.start()
	try:
		while True:
			time.sleep(2)
	except (KeyboardInterrupt,SystemExit):
		scheduler.shutdown()
