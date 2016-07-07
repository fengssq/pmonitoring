#coding:utf8
#time:'下午2:12:16-7-4:2016'
#author:Gru_GHT
#为测试ela插入测试。

from libs.rules import *
from libs.config import *



import scapy.all as scapy

packets=scapy.rdpcap('/var/log/3moon/t_00001_20160704162153.pcap')

aa=regx_raw()
#print 'host:'+aa.regx_host(packets[5322]['Raw'].load) 获取host
num=0
#显示全部url地址
for i in range(len(packets)):
    try:
        #print 'http://'+aa.regx_host(packets[i]['Raw'].load)+aa.regx_sql(packets[i]['Raw'].load)
        #print re.findall(r'(?i)(and|select|union)\W.*(?i)(select|char|union)',aa.regx_sql(packets[i]['Raw'].load).split()[0])

        if aa.sql_inject(aa.regx_sql(packets[i]['Raw'].load).split()[0])==None:
            pass
        elif aa.sql_inject(aa.regx_sql(packets[i]['Raw'].load).split()[0])==100:
            #print '入侵警报：'+aa.regx_sql(packets[i]['Raw'].load).split()[0]
            urlt='"%s"' %aa.regx_sql(packets[i]['Raw'].load).split()[0]
            urltype='"%s"' %aa.regx_sql(packets[i]['Raw'].load).split()[1]
            #计数为插入id准备
            num=num+1
            urlhost='"%s"' % aa.regx_host(packets[i]['Raw'].load)
            srcip='"%s"' % packets[i]['IP'].src
            #装载插入数据信息
            bb=rawurltt()
            bb.insurl(num,urlt,urltype,srcip,urlhost,'1','a')
    except:
        pass

print '---------------'
