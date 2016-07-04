#coding:utf8
#time:'下午2:59:16-6-27:2016'
#author:Gru_GHT

import os,sys,time,re,stat
import scapy.all as scapy
import libs.rules
#sys.stdout=open('kk.txt', 'wr')

global filelist
filelist=[]
class code_un():
    def num_list(self,dir):
        if len(os.listdir(dir))-1<1:
            pass
        else:
            return '1'
    def dirplay(self,dir):
        for i in os.listdir(dir):
            i='/var/log/3moon/'+i
            if os.path.getsize(i)>1000000 or os.stat(i).st_mode==33152:
                filelist.append(i)

    def en_code(self,d_file):
        regx=r'[A-Z]{3,4}.*?\ HTTP'
        d_packet=scapy.rdpcap(d_file)
        for i in xrange(len(d_packet)):
            try:
                if d_packet[i]['Raw'].load.startswith('GET') or d_packet[i]['Raw'].load.startswith('POST'):
                    print d_packet[i]['IP'].src,'==>',d_packet[i]['IP'].dst,re.findall(regx,d_packet[i]['Raw'].load)[0]
                else:
                    pass
            except:
                pass

a=code_un()
import gc
while True:
    time.sleep(1)
    try:
        if a.num_list('/var/log/3moon/')==None:
            del filelist[:]
        else:
            a.dirplay('/var/log/3moon/')
        for i in filelist:
            #i='/var/log/3moon/'+i
            a.en_code(i)
            commands='rm -rf %s'%i
            os.system(commands)
    except:
        pass
    gc.collect()