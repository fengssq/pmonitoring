#coding:utf8
#time:'下午6:09:16-7-4:2016'
#author:Gru_GHT
#info: Elasticsearch

from elasticsearch import Elasticsearch
from elasticsearch import helpers

es=Elasticsearch()

class rawurltt():

    def insurl(self,rawid,rawurl,rawtype,rawsrcip,rawhost,rawpostdata,rawcookiedb):
        dd=[]
        rawdata='urltest'
        sdata={"url":rawurl,"type":rawtype,"srcip":rawsrcip,"srchost":rawhost,"srcpost":rawpostdata,"srcookie":rawcookiedb}
        valuea={
            "_index":rawdata,
            "_type":"utext",
            "_id":rawid,
            "_source":sdata
            }
        dd.append(valuea)
        try:
            helpers.bulk(es,dd)
            print 'The rotation is complete!'
        except Exception,e:
            print 'Error:',e
            print 'The rotation is Error!'










