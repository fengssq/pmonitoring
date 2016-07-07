#coding:utf8
#time:'下午2:41:16-7-5:2016'
#author:Gru_GHT

from elasticsearch import Elasticsearch
from  datetime import datetime
import json
es=Elasticsearch("127.0.0.1")
raw_type='TRACER'
rawdata="testt"
raw_host="www.kuwo.cn"
raw_url="/adf?afasd.php/http://a.com/a.jpg/tsth=1"
raw_cookie=""
raw_post=""
#len(es.indices.create(index=a,ignore=400))==2 判断长度为2就可以判断错误出现。
#print es.indices.delete(index=a,ignore=[400,404])
#print len(es.indices.create(index=a,ignore=400))
#print es.indices.create(index=rawdata,body={"type":raw_type,"src_ip":raw_host,"url":raw_url,"post":raw_post,"cookie":raw_cookie},ignore=400)
#print es.indices.create(index=rawdata,ignore=400)
#es.create(index=rawdata,id=1,doc_type="test-type",body={"type":raw_type,"src_ip":raw_host,"url":raw_url,"post":raw_post,"cookie":raw_cookie},ignore=400)
#es.create(index=rawdata,id=3,doc_type="test-type",body={"type":raw_type,"src_ip":raw_host,"url":raw_url,"postdata":raw_post,"cookie":raw_cookie},ignore=400)
#print es.get(index=rawdata,id=2)['_source']

#print 'body={"type":"%s","src_ip":"%s","url":"%s","postdata":"%s","cookie":"%s"}' %(raw_id,raw_type,rawdata,raw_host,raw_url,raw_cookie,raw_post)
#print es.search(index=rawdata)
#print es.indices.create(index=rawdata,ignore=400)
#print es.indices.delete(index=rawdata)
#print es.create(index="rawurltest",id=790,doc_type="test-type",}



from elasticsearch import helpers
#b=[]
dd=[]
a={
    "_index":rawdata,
    "_type":"urltext",
    "_id":1,
    "_source":{
        "url":"http://a.co.cn",
        "type":"GET",
        "srcip":"1.1.1.1",
        "srchost":"kuwo.cn",
    }
}

dd.append(a)
#helpers.bulk(es,dd)

print es.get(index=rawdata,id=1)