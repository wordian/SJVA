# -*- coding: utf-8 -*-
#########################################################
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugin'))
# 반드시 필요. websocket. 없는 경우 ping_interval 주기로만 통신함. thread=false 넣으면 안됨.
try:
    from gevent import monkey;monkey.patch_all()
except:
    print 'not monkey'


######################################
# docker_start.sh 에 site.db로 되어 있어 migration 안되고 있음
try:
    import os
    site_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'db', 'site.db')
    
    print site_db
    if not os.path.exists(site_db):
        print 'site.db file not exist!!'
        f = open(site_db, 'w')
        f.close()
        sys.exit("1")
    else:
        print 'site.db file exist!!'
    tmp = '/app/bin/Linux'
    if os.path.exists(tmp):
        for t in os.listdir(tmp):
            os.chmod(os.path.join(tmp, t), 0755)
            print 'CHMOD : %s' % t
except Exception, e:
    print('Exception:%s', e)



import framework
import system


   
app = framework.app
#celery = framework.celery
#socketio = framework.socketio
 
"""
try:
    from ddtrace import patch_all
    patch_all()
except:
    pass
"""
# update:1
# restart:2



def start_app():
    for i in range(5):
        try:
            framework.socketio.run(app, host='0.0.0.0', port=app.config['config']['port'])
            print 'EXIT CODE : %s' % framework.exit_code
            if framework.exit_code != -1:
                sys.exit(framework.exit_code)
                break
            else:
                print 'framework.exit_code is -1'
            
            break
        except Exception as e:
            print e
            import time
            time.sleep(3*i)
            continue
        except KeyboardInterrupt:
            print 'KeyboardInterrupt !!'
    print 'start_app() end'

if __name__ == '__main__':
    try:
        start_app()
    except Exception as e:
        print e
        
