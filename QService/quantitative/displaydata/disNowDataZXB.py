# coding=utf-8
'''
@author: ElegyPrincess
'''
import json
from django.http import HttpResponse
import NowData as ND
def display_now_zxb_price(request):
        stock = "zxb"
        data = ND.nowPrice(stock)
        #查询出来是空值会怎么样
        jsondatar = json.dumps(data, ensure_ascii=False)
        return HttpResponse(jsondatar,content_type='application/json')

def display_now_zxb(request):
    stock = "zxb"
    data = ND.nowData(stock)
    # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
    # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
    # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
    jsondatar = json.dumps(data, ensure_ascii=False)
    return HttpResponse(jsondatar, content_type='application/json')

