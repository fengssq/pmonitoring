#coding:utf8
#time:'下午3:32:16-7-29:2016'
#author:Gru_GHT

from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json

es=Elasticsearch()
a=es.search(index='urltest')['hits']['total']
#print a['hits']
print json.dumps(es.get(index='urltest',id=1500))
a=es.search(index='urltest')['hits']['total']
#print a['hits']
for i in range(1,a+1):
    tr=es.get(index='urltest',id=i)
