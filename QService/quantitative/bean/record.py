#coding=utf-8

class record(object):
    def __init__(self,date,term,invest,stock):
        self.date=date
        self.term=term
        self.invest=invest
        if stock=='sh_hist_data':
            self.stock=0
        elif stock=='sz_hist_data':
            self.stock=1
        elif stock=='sz50_hist_data':
            self.stock=2
        elif stock=='hs300_hist_data':
            self.stock=3
        elif stock=='cyb_hist_data':
            self.stock=4
        elif stock=='zxb_hist_data':
            self.stock=5
        else:
            self.stock=-1