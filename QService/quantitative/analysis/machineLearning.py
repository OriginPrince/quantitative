#coding=utf-8
import MySQLdb
import numpy as np
from sklearn.svm import SVR

def MaLearning(stock,dayCount):
    #从数据库查询出来数据做SVM回归预测
    conn = MySQLdb.Connect(host='localhost', user='root', passwd='888212', db='economic', port=3306, charset='utf8')
    cur = conn.cursor()
    sql = "SELECT close FROM "+stock+" order by date"
    cur.execute(sql)
    result = cur.fetchall()
    #print result
    cur.close()
    conn.close()

    data = np.mat(result)
    data = data.ravel()
    data = np.array(data[0])
    # print u'数据：',data

    i = 0
    reRate = []
    sumValule = []
    sum = 0

    #计算以dayCount为时间间隔的数据和
    for j in data[0]:
        sum += j
        i = i + 1
        if str(i)==dayCount:
            sumValule.append(sum)
            #print "添加"+str(sum)
            i = 0
            sum = 0

    #print u'总和：',sumValule
    #计算收益率
    k = 0
    while k < (len(sumValule) - 1):
        rate = (sumValule[k + 1] - sumValule[k]) / sumValule[k]
        k = k + 1
        reRate.append(rate)

    print u'增长率：', reRate
    #使用收益率来做预测
    X = np.array(range(0, len(reRate)))
    X = np.mat(X)
    X = X.transpose()

    y = np.array(reRate)

    #print u'数据：', X.shape, y.shape

    ###############################################################################
    # Fit regression model
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    # svr_lin = SVR(kernel='linear', C=1e3)
    # svr_poly = SVR(kernel='poly', C=1e3, degree=2)

   # y_rbf = svr_rbf.fit(X, y).predict(X)
    # y_lin = svr_lin.fit(X, y).predict(X)
    # y_poly = svr_poly.fit(X, y).predict(X)

    pr = svr_rbf.fit(X, y).predict([[len(reRate)]])
    #预测出股指收益率
    print "预测收益率：",pr
    return pr
