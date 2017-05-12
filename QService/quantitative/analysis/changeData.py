# coding=utf-8
'''
Created on 2016-10-26
@author: Jennifer
Project:读取mysql数据库的数据，转为json格式
'''
import MySQLdb
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from calculate import calFinal as CF
import Data as DO
import time
import threading
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def job(inRate,terms,ulInvest,dayCount,id_plan):
    stock = "cyb_hist_data"
    stock_id='150152'
    result = CF(inRate, terms, ulInvest, dayCount,stock,id_plan,stock_id)
    if result == "not proper":
        print result
    elif result=="error":
        print result
    elif result=="ok":
        print result
    elif result=="over":
        print result
        jobID = 'my_job' + str(id_plan)
        scheduler.remove_job(jobID)
        m=DO.change_over(id_plan)[0]
        if m==0:
            print "修改失败"
        else:
            print "修改成功"

    else:
        pass

class threadRecord(threading.Thread):
    def __init__(self,inRate,terms,ulInvest,dayCount,id_plan):
        threading.Thread.__init__(self)
        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.inRate=inRate
        self.terms=terms
        self.ulInvest=ulInvest
        self.dayCount=dayCount
        self.id_plan=id_plan
        self.Isflag=True

    def run(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            jobID='my_job'+str(self.id_plan)
            print jobID
            scheduler.add_job(job, 'interval', args=(self.inRate,self.terms,self.ulInvest,self.dayCount,self.id_plan),seconds=5 , id=jobID)
            scheduler.start()
            try:
                while self.Isflag:
                    time.sleep(86400)
                    data=DO.Data_over(self.id_plan)
                    self.Isflag=data[0]

            except (KeyboardInterrupt, SystemExit):
                scheduler.shutdown()

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()

@csrf_exempt
def change_final(request):
    if request.POST:
        ulInvest = request.POST['FulInvest']
        ulInvest=str(ulInvest)
        terms = request.POST['Fterms']
        inRate = request.POST['FinRate']
        inRate=str(inRate)
        taxRate = request.POST['FtaxRate']
        dayCount = request.POST['FdayCount']
        id_user=request.session['userid']
        print inRate
        tempTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        tempClass=1
        tempAlterms=0
        tempVolume=0
        tempAlInvest=0
        tempover=1
        n=0
        try:
            conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306,
                                   charset='utf8')
            cur = conn.cursor()
            sql1 = "insert into valueplan (ultimateInvest,rateInvest,terms,dayCount,id_user,class,time,alterms,volume,alInvest,over) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            n = cur.execute(sql1, (ulInvest, inRate, terms, dayCount,id_user,tempClass,tempTime,tempAlterms,tempVolume,tempAlInvest,tempover))
            conn.commit()
            sql2 = "select id from valueplan where time = %s"
            cur.execute(sql2, (tempTime))
            data=cur.fetchall()
            id_plan=data[0][0]
            cur.close()
            conn.close()
            print id_plan
            threadRE = threadRecord(inRate, terms, ulInvest, dayCount, id_plan)
            # 调用子线程来执行定时任务，定投
            threadRE.start()
        except:
            print 'MySQL connect fail...'
        if n != 1:
            print "插入错误"
            return HttpResponse("false")
        else:
            return HttpResponse("true")
    else:
        print "未获取到数据"
        return HttpResponse("no data")

alert=[1]

@csrf_exempt
def change_initial(request):
    alert[0]=alert[0]+1
    print alert[0]
    return HttpResponse(alert[0])