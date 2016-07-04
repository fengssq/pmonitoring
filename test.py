#coding:utf8
#time:'下午2:12:16-7-4:2016'
#author:Gru_GHT

from libs.rules import *




import scapy.all as scapy

packets=scapy.rdpcap('/var/log/3moon/t_00024_20160704114951.pcap')

aa=regx_raw()
#print 'host:'+aa.regx_host(packets[5322]['Raw'].load) 获取host
print aa.regx_host(packets[5322]['Raw'].load)+aa.regx_sql(packets[5322]['Raw'].load)
#显示全部url地址