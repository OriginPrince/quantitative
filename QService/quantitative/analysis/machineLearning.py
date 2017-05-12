#coding=utf-8
import MySQLdb
import numpy as np
from sklearn.svm import SVR

def MaLearning(stock,dayCount):
    # 1-7：如何使用python DB API访问数据库流程的
    # 1.创建mysql数据库连接对象connection
    # connection对象支持的方法有cursor(),commit(),rollback(),close()
    conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
    # 2.创建mysql数据库游标对象 cursor
    # cursor对象支持的方法有execute(sql语句),fetchone(),fetchmany(size),fetchall(),rowcount,close()
    cur = conn.cursor()
    # 3.编写sql
    # sql = 'SELECT date,open,close,low,high,volume,amount FROM cyb_hist_data where date="'+request.GET['date']+' 00:00:00"'
    sql = "SELECT close FROM "+stock+" order by date"
    # 4.执行sql命令
    # execute可执行数据库查询select和命令insert，delete，update三种命令(这三种命令需要commit()或rollback())
    cur.execute(sql)
    # 5.获取数据
    # fetchall遍历execute执行的结果集。取execute执行后放在缓冲区的数据，遍历结果，返回数据。
    # 返回的数据类型是元组类型，每个条数据元素为元组类型:(('第一条数据的字段1的值','第一条数据的字段2的值',...,'第一条数据的字段N的值'),(第二条数据),...,(第N条数据))
    result = cur.fetchall()
    print result

    # 6.关闭cursor
    cur.close()
    # 7.关闭connection
    conn.close()

    data = np.mat(result)
    data = data.ravel()
    data = np.array(data[0])
    # print u'数据：',data

    i = 0
    reRate = []
    sumValule = []
    sum = 0
    #print type(dayCount)
    for j in data[0]:
        sum += j
        i = i + 1
        if str(i)==dayCount:
            sumValule.append(sum)
            #print "添加"+str(sum)
            i = 0
            sum = 0

    print u'总和：',sumValule

    k = 0
    while k < (len(sumValule) - 1):
        rate = (sumValule[k + 1] - sumValule[k]) / sumValule[k]
        k = k + 1
        reRate.append(rate)

    print u'增长率：', reRate

    X = np.array(range(0, len(reRate)))
    X = np.mat(X)
    X = X.transpose()

    y = np.array(reRate)

    print u'数据：', X.shape, y.shape

    ###############################################################################
    # Fit regression model
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    # svr_lin = SVR(kernel='linear', C=1e3)
    # svr_poly = SVR(kernel='poly', C=1e3, degree=2)

   # y_rbf = svr_rbf.fit(X, y).predict(X)
    # y_lin = svr_lin.fit(X, y).predict(X)
    # y_poly = svr_poly.fit(X, y).predict(X)

    # id=data[-1,0]+1
    # print id
    pr = svr_rbf.fit(X, y).predict([[len(reRate)]])
    #预测出股指收益率

    return pr
