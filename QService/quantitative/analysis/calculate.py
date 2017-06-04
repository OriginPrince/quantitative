#coding=utf-8
'''
@author:ElegyPrince
@project：计算投资数据
'''
import MySQLdb
import Data as DA
import tushare as ts
import time
import machineLearning as ml
import random

#进行情景二的投资计算
def calculateAl(inRate,T,t,ulInvest,dayCount,stock,id_plan,stock_id,taxRate):#计算价值目标，参数：投资增长率，总期数，总额度，时间间隔，股指，对应投资计划的id，股指基金代码
    #输出的时候数据要转化成字符串
    print "获取的数据   inRate："+str(inRate)+"  T："+str(T)+"  ulInvest："+str(ulInvest)+"  dayCount："+str(dayCount)+"  stock："+str(stock)+"  id_plan："+str(id_plan)+"  stock_id："+str(stock_id)
    reRate = ml.MaLearning(stock, dayCount)[0]#是个数组
    inRate=float(inRate)#投资增长率，注意获取的数据需要转化成可用的形式
    T=int(T)#总期数
    t=int(t)#计算中使用的当前期数
    ulInvest=float(ulInvest)#总额度
    taxRate=float(taxRate)

    if reRate > 0:
        data = DA.Data(id_plan)
        alInvest = float(data[0][0])#已经投资的总额
        alVolume = float(data[0][1])#已经投资的份数
        alterms = int(data[0][2])#已经投资的次数
        alterms=alterms+t#计算中已经投资了多少次
        term=alterms+1#计算时候所使用的本次是第几次投资
        tempDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print "ccc   " + str(alInvest) +  "  " + str(alInvest) + "  " + str(alVolume)
        if alterms>=T:
            return "over"
        else:
            R = (reRate + inRate) / 2
            A = pow((1 + R), T)
            Invest = ulInvest / (T * A)# 每期投资的价值目标C
            TInvest=Invest*term*pow((1+R),term)#账户此时应该拥有的总价值

            fd=ts.get_realtime_quotes(stock_id)
            price=float(fd['price'])#每股的价格
            #price = random.uniform(0.9, 1.2)#模拟计算的
            NeedInvest=TInvest-alVolume*price#本次投资的金额
            NeedVolume=NeedInvest/price#本次投资的份额

            #只对卖出所得的实际收入进行收税
            #if NeedInvest<0:
            #    NeedInvest=NeedInvest*(1-taxRate)

            alVolume=alVolume+NeedVolume#在计划表中重新计算已经投资的总份额
            alInvest=alInvest+NeedInvest#在计划表中重新记录已经投资的总金额
            n=0
            m=0
            term=term-t#记录的本次是第几次投资
            print "投资数据   NeedInvest：" + str(NeedInvest) + "  NeedVolume：" + str(NeedVolume) + "  alInvest：" + str(alInvest)+ "  alVolume：" + str(alVolume)
            try:
                conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306,
                                       charset='utf8')
                cur = conn.cursor()
                sql1 = "insert into record (date,term,invest,volume,id_plan,stock) values (%s,%s,%s,%s,%s,%s)"
                n = cur.execute(sql1, (tempDate,term,NeedInvest,NeedVolume, id_plan,stock))
                conn.commit()
                sql2 = "update valueplan set alInvest=%s,alterms=%s,volume=%s where id=%s"
                m = cur.execute(sql2, (alInvest, term, alVolume,id_plan))
                conn.commit()
                cur.close()
                conn.close()
            except:
                print '投资记录 MySQL connect fail...'
            print m,n
            if (n == 1)&(m==1):
                return "ok"
            else:
                return "error"
    else:
        return "not proper"


#进行情景二的投资计算
def calculate(inRate,terms,ulInvest,dayCount,stock,id_plan,stock_id,taxRate):#计算价值目标，参数：投资增长率，总期数，总额度，时间间隔，股指，对应投资计划的id，股指基金代码
    #输出的时候数据要转化成字符串
    print "获取的数据   inRate："+str(inRate)+"  terms："+str(terms)+"  ulInvest："+str(ulInvest)+"  dayCount："+str(dayCount)+"  stock："+str(stock)+"  id_plan："+str(id_plan)+"  stock_id："+str(stock_id)
    reRate = ml.MaLearning(stock, dayCount)[0]#是个数组
    inRate=float(inRate)#投资增长率，注意获取的数据需要转化成可用的形式
    terms=int(terms)#总期数
    ulInvest=float(ulInvest)#总额度
    taxRate=float(taxRate)

    if reRate > 0:
        data = DA.Data(id_plan)
        alInvest = float(data[0][0])#已经投资的总额
        alVolume = float(data[0][1])#已经投资的份数
        alterms = int(data[0][2])#已经投资的次数
        term=alterms+1#本次是第几次投资
        tempDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print "ccc   " + str(alInvest) +  "  " + str(alInvest) + "  " + str(alVolume)
        if alterms>=terms:
            return "over"
        else:
            R = (reRate + inRate) / 2
            A = pow((1 + R), terms)
            Invest = ulInvest / (terms * A)# 每期投资的价值目标C
            TInvest=Invest*term*pow((1+R),term)#账户此时应该拥有的总价值

            fd=ts.get_realtime_quotes(stock_id)
            price=float(fd['price'])#每股的价格
            NeedInvest=TInvest-alVolume*price#本次投资的金额
            NeedVolume=NeedInvest/price#本次投资的份额

            #只对卖出所得的实际收入进行收税
            #if NeedInvest<0:
            #    NeedInvest=NeedInvest*(1-taxRate)

            alVolume=alVolume+NeedVolume#在计划表中重新计算已经投资的总份额
            alInvest=alInvest+NeedInvest#在计划表中重新记录已经投资的总金额
            n=0
            m=0
            print "投资数据   NeedInvest：" + str(NeedInvest) + "  NeedVolume：" + str(NeedVolume) + "  alInvest：" + str(alInvest)+ "  alVolume：" + str(alVolume)
            try:
                conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306,
                                       charset='utf8')
                cur = conn.cursor()
                sql1 = "insert into record (date,term,invest,volume,id_plan,stock) values (%s,%s,%s,%s,%s,%s)"
                n = cur.execute(sql1, (tempDate,term,NeedInvest,NeedVolume, id_plan,stock))
                conn.commit()
                sql2 = "update valueplan set alInvest=%s,alterms=%s,volume=%s where id=%s"
                m = cur.execute(sql2, (alInvest, term, alVolume,id_plan))
                conn.commit()
                cur.close()
                conn.close()
            except:
                print '投资记录 MySQL connect fail...'
            print m,n
            if (n == 1)&(m==1):
                return "ok"
            else:
                return "error"
    else:
        return "not proper"