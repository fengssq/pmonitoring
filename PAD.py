#coding:utf8
#time:'下午2:59:16-6-27:2016'
#author:Gru_GHT

import os,sys,time,re,stat
import scapy.all as scapy
from libs.rules import *
from db.config import *
#sys.stdout=open('kk.txt', 'wr')

global filelist
filelist=[]

coun_num=0
#需要添加计数器，为方便插入id数值
class code_un():
    def en_code(self,d_file):
        '''主操作，加载参数过滤并展示信息'''
        global coun_num
        #增加数据库计数器
        regx=r'[A-Z]{3,4}.*?\ HTTP'
        d_packet=scapy.rdpcap(d_file)
        one_regx=regx_raw()
        for i in xrange(len(d_packet)):
            #获取每一个数据包信息
            try:
                if d_packet[i]['Raw'].load.startswith('GET'):

                    vlue_s,snffer_url=one_regx.attack_url(d_packet[i]['Raw'].load)
                    shost=one_regx.regx_host(d_packet[i]['Raw'].load)
                    sscrip=d_packet[i]['IP'].src
                    #coun_num=coun_num+1
                    #print coun_num
                    if vlue_s=='100' or vlue_s=='200':
                        print '警告',snffer_url
                        dd.insurl(coun_num,snffer_url,'GET',sscrip,one_regx.regx_host(d_packet[i]['Raw'].load),'1','A')
                    else:
                        print '正常：',snffer_url
                        pass
                '''
                if d_packet[i]['Raw'].load.startswith('GET') or d_packet[i]['Raw'].load.startswith('POST'):
                    print d_packet[i]['IP'].src,'==>',d_packet[i]['IP'].dst,re.findall(regx,d_packet[i]['Raw'].load)[0]
                    print d_packet[i]['Raw'].load
                else:
                    pass
                '''
            except:
                pass

    def file_list(self,dir):
        '''获取当前目录中信息，剔除正在生成文件'''
        for i in os.listdir(dir):
            i='/var/log/3moon/'+i
            if os.path.getsize(i)>1000000 and os.stat(i).st_mode==33152:
                filelist.append(i)
            else:
                #print '正在获取中...'
                pass
a=code_un()
dd=rawurltt()
import gc
if __name__=='__main__':

    print '请检查ela分布式是否开启，检查sqlmap是否启动服务。完毕后请刷新验证再次启动' \
          '启动完毕后，请先执行db目录中的createdb.py，再次执行PAD！'
    if raw_input('请确认：\n')=='y':
        print '开启轻量安全分析插件'
        print '本次分析基准：安全信息仅展示，存在攻击或异常将保存至服务器！'
        while True:
            time.sleep(1)
            try:
                a.file_list('/var/log/3moon/')
                #print len(filelist)

                if len(filelist)<0 or len(filelist)==0:
                    print '正在获取信息中...'
                else:
                    #'''
                    for i in filelist:
                        a.en_code(i)
                        commands='rm -rf %s'%i
                        os.system(commands)
                    #'''执行完毕后清空列表，留待再次获取数据
                    del filelist[:]

            except Exception,e:
                print e
            gc.collect()
    else:
        print '请再次检查后启动该程序后台运行！'