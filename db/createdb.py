#coding:utf8
#time:'下午2:41:16-7-5:2016'
#author:Gru_GHT

from elasticsearch import Elasticsearch

es=Elasticsearch()
#print es.search(index='urltest')
#print es.indices.get(index='urltest')
#print es.indices.delete(index='urltest')
#print es.indices.create(index='urltest',ignore=400)
def main():

    try:
        if es.indices.create(index='urltest',ignore=400)['status']==400:
            print '已经存在'
            if raw_input('请确认是否删除新建:\n')=='y':
                es.indices.delete(index='urltest')
                if es.indices.create(index='urltest',ignore=400)['acknowledged']==True:
                    print '重置成功！'
                else:
                    print '创建失败，请检查服务是否启动！'
            else:
                print '请再次检查确认！'
                pass
        else:
            print 'a'

    except Exception,e:
        #print '请检查服务是否启动'
        if es.indices.create(index='urltest',ignore=400):
                print '创建成功！'
        else:
                print '创建失败，请检查服务是否启动！'
        #print e,'请检查服务是否启动！'
if __name__=='__main__':
    print 'Elasticsearch 数据库创建审查。请谨慎确认！一经覆盖无法修复！'
    main()
