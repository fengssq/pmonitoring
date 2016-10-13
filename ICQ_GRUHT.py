#coding:utf8
#time:'上午11:20:16-10-12:2016'
#author:Gru_GHT

import socket,time,sys,os,re
import datetime
def s_server():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    socket.gethostbyname(socket.gethostname()) #当前ip
    l_hostname=socket.gethostname() #主机名
    s.settimeout(100)
    n=datetime.datetime.now()
    send_time= n.strftime('%Y%m%d-%H:%M:%S')
    print ' %s HIVE OPEN'%l_hostname
    s.bind(('',5513))
    s.listen(1)
    while 1:
        cdata,caddr=s.accept()
        print 'bee alreay online '+caddr[0].strip()
        ip=caddr[0].strip()
        while 1:
            client_data=cdata.recv(4096)
            if not client_data:
                break
            client_conten='CCC>>> %s:%s'%(send_time,client_data.strip())
            print client_conten
            cdata.send(client_conten+'\n')

            l_data=raw_input('L>>>')
            if l_data:
                local_data='DDD>> %s:%s'%(send_time,l_data.strip())
                cdata.send(local_data+'\n')
            else:
                break

    cdata.close()
    s.close()

def se_data(ipp):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.gethostbyname(socket.gethostname()) #当前ip
    l_hostname=socket.gethostname() #主机名
    s.settimeout(100)
    n=datetime.datetime.now()
    send_time= n.strftime('%Y%m%d-%H:%M:%S')
    print ' %s BEE START GET INTO!\n'%l_hostname
    try:
        s.connect((ipp,5513))
        s.send('BEE ALREADY GET INTO!')
        while 1:
            try:
                d= s.recv(1024)
                print d
            except:
                pass
            send_data=raw_input('LLL>>>').strip()
            s.send(send_data)
            print 'LLL>>> %s:%s'%(send_time,send_data.strip()+'\n')
            #print s.recv(1024)
        s.close()
    except socket.error,e:
        print '请确认服务器是否开启，或防火墙拦截！'

if __name__=='__main__':
    num=raw_input('PLEASE 1 OR 0\n')
    if num=='1':
        print '本机为客户端，请填写服务器IP'
        ipt=raw_input('IP:\n').strip()
        se_data(ipt)
    elif num=='0' :
        print '本机为服务器，请告知客户端IP'
        s_server()
    else:
        sys.exit()