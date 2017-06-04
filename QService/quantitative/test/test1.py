# coding=utf-8
import tushare as ts
import MySQLdb
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy import create_engine
engine=create_engine('mysql://root:888212@127.0.0.1/economic?charset=utf8')
sh_df = ts.get_h_data('000001', index=True, start='2017-01-01', end='2017-02-01')
sh_df['stock']='sh'
sh_df.to_sql('histdata', engine, if_exists='append')
print "insert successfully"