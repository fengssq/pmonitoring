#coding:utf8
#time:'下午2:50:16-7-4:2016'
#author:Gru_GHT
#info: using sql injection

import urllib2,cookielib
#31323131323132
import requests,json,time
global idtext
idtext=[]
#please start sqlmapapi -s -H 127.0.0.1
class sql_att():
    def __init__(self,id,url,post,cookie):
        self.id=id
        self.url=url
        self.post=post
        self.cookie=cookie
        self.start_time=time.time()
        self.master_id=31323131323132
        self.master_url='http://127.0.0.1:8775'
    #获取id
    def start_new(self):
        self.task_id=json.loads(requests.get(self.master_url+'/task/new').text)['taskid']
        return self.task_id
    #特定id执行扫描
    def start_scan(self):
        self.start_scan_id=self.start_new()
        smaster='http://127.0.0.1:8775/scan/'+self.start_scan_id+'/start'
        attack_url={'url':self.url}
        aheaders={'Content-Type':'application/json'}
        if json.loads(requests.post(smaster,data=json.dumps(attack_url),headers=aheaders).text)['success']:
            return self.start_scan_id
        else:
            return False
    #特定ip审核状态
    def start_status(self):
        #status_url='http://127.0.0.1:8775/scan/'+self.start_scan_id+'/status'
        status_url='http://127.0.0.1:8775/scan/604eec6ccb20635d/status'
        if json.loads(requests.get(status_url).text)['status']=='terminated':
            print '已经结束,请检查报告'
    #特定ip获取结果
    def start_data(self):
        #start_data_url='http://127.0.0.1:8775/scan/'+self.start_scan_id+'/data'
        start_data_url='http://127.0.0.1:8775/scan/604eec6ccb20635d/data'
        if json.loads(requests.get(start_data_url).text)['data']:
            print '存在注入点'

    def sql_main(self):
        self.db=[]
        try:
            #if self.start_new()>0:
            if self.start_scan():
                print 'Strat testing:',self.url,self.start_scan_id
                self.db.append(self.start_scan_id)
            else:
                print 'cuowu'
        except Exception,e:
            print 'Error: ',e
    def list_taskid(self):
        print self.db
a=sql_att(1,'http://www.g.re/Less-1/?id=1',3,4)
a.sql_main()
#a.list_taskid()
#a.start_scan()
#a.start_status()
#a.start_data()