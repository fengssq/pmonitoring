#coding:utf8
#time:'上午10:46:16-7-4:2016'
#author:Gru_GHT

import re,os,sys

class regx_raw():
    def regx_host(self,raw_vlue):
        re_host=r'Host: .*\r\n'
        try:
            raw_host= re.findall(re_host,raw_vlue)[0].split()[1]
            return raw_host
        except:
            pass
    def regx_url(self,raw_vlue):
        regx=r'[A-Z]{3,4}.*?\ HTTP'
        try:
            #if re.findall(regx,raw_vlue).
            pass
        except:
            pass
    def regx_sql(self,raw_vlue):
        regx_sql_url=r'[A-Z]["GET","POST"].*\?.* HTTP\/1.1'
        #regx=r'[A-Z]{3,4}.*?\ HTTP'
        return re.findall(regx_sql_url,raw_vlue)[0].split()[1]

