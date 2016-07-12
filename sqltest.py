#coding:utf8
#time:'下午2:43:16-7-7:2016'
#author:Gru_GHT

from libs.sqlmapapp import *
url='http://www.g.re/Less-1/?id=1'

import requests,json
a=requests.get('http://127.0.0.1:8775/admin/31323131323132/list')
print a.json()['tasks']