#coding:utf8
#time:'上午10:46:16-7-4:2016'
#author:Gru_GHT
#info: web information fifter rules

import re,os,sys
global tts,rurl
rurl=[]
tts=[]
class regx_raw():
    def regx_host(self,raw_vlue):
        re_host=r'Host: .*\r\n'
        try:
            raw_host= re.findall(re_host,raw_vlue)[0].split()[1]
            return raw_host
        except:
            pass
    def regx_url(self,raw_vlue):
        '''this is extract url'''
        regx=r'[A-Z]{3,4}\ .*?HTTP\/1.1'
        return re.findall(regx,raw_vlue)[0].split()[1]
    def regx_sql(self,raw_vlue):
        '''this is extract /? url, using sqlmapapi'''
        regx_sqlapi_url=r'[A-Z]{3,4}\ .*\?.*?HTTP\/1.1'
        tts.append(re.findall(regx_sqlapi_url,raw_vlue)[0].split()[1])
        return re.findall(regx_sqlapi_url,raw_vlue)[0].split()[1]+' '+re.findall(regx_sqlapi_url,raw_vlue)[0].split()[0]
    def sql_inject(self,vlue_sql):
        self.value_sql_url=self.regx_url(vlue_sql)

        regx_sql_url=r'(?i)(and|select|union)\W.*(?i)(select|char|union)'
        regx_sql_url_one=r'(?i)sleep\('
        regx_sql_url_two=r'(?i)ord\(mid'
        if re.findall(regx_sql_url,self.value_sql_url):
            return 100
        elif re.findall(regx_sql_url_one,vlue_sql):
            return 100
        elif re.findall(regx_sql_url_two,vlue_sql):
            return 100
        else:
            pass
    def xss_attack(self,xss):
        self.xss=xss
        regx_xss=r'(?i)alert\('
        if re.findall(regx_xss,xss):
            return 200
    def attack_url(self,url):
        if self.xss_attack(url)==200:
            print '200',self.xss
        elif self.sql_inject(url)==100:
            return '100',self.value_sql_url
        else:
            return '3',self.regx_url(url)