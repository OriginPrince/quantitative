#coding=utf-8

import hashlib

def md5(str):
    m=hashlib.md5()
    m.update(str)
    return m.hexdigest()
