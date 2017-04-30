# coding=utf-8
import threading  
import tushare as ts
from sqlalchemy import create_engine
import time
from apscheduler.schedulers.background import BackgroundScheduler

timer_interval=1

engine=create_engine('mysql://root:888212@127.0.0.1/economic?charset=utf8')

class threadHS300(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.__flag = threading.Event()     # 用于暂停线程的标识
        self.__flag.clear()       # 设置为True
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()      # 将running设置为True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            df=ts.get_realtime_quotes('hs300')
            df[['open','price','high','low','volume','amount','date','time']].to_sql('hs300_now_data',engine,if_exists='append')
            print df  
            time.sleep(1)

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()
		

threadhs300 = threadHS300()

				 
def start_job():
    threadhs300.start()
    print("start")	
    
def stop_job():
    threadhs300.stop()
    
def pause_morning_job():
    threadhs300.pause()
    print("pause morning")
	
def pause_afternoon_job():
    threadhs300.pause()
    print("pause morning")
	
def resume_morning_job():
    threadhs300.resume()
    print("resume morning")

def resume_afternoon_job():
    threadhs300.resume()
    print("resume morning")

def deleteAll_job():
    engine.execute("truncate table hs300_now_data")
    print("truncate table")
	
   
if __name__=="__main__":
    start_job()
    scheduler = BackgroundScheduler()
    scheduler.add_job(resume_morning_job, 'cron', day_of_week='mon-fri', hour=9, minute=30)
    scheduler.add_job(pause_morning_job, 'cron', day_of_week='mon-fri', hour=11, minute=30)
    scheduler.add_job(resume_afternoon_job, 'cron', day_of_week='mon-fri', hour=13, minute=00)
    scheduler.add_job(pause_afternoon_job, 'cron', day_of_week='mon-fri', hour=15, minute=00)
    scheduler.add_job(deleteAll_job, 'cron', day_of_week='mon-fri', hour=9, minute=25)
    scheduler.start()
	
    t=time.strftime("%H:%M:%S",time.localtime(time.time()))
    day=time.strftime('%A')
    weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday']
    flagDay=False
    if day in weekdays:
        flagDay=True
    if (t>'09:30:00' and t<'11:30:00' and flagDay is True) or (t>'13:00:00' and t<'15:00:00' and flagDay is True):
        resume_morning_job()
    flag=True
    try:
        while flag is True:
            time.sleep(2)
            if threadhs300.isAlive():
                pass
            else:
                flag=False
            print flag
    except (KeyboardInterrupt,SystemExit):
        scheduler.shutdown()
