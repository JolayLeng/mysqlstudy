 
#!/usr/bin/python2.7
# -*- coding:utf-8 -*-
# create : 2014-7-22
# 数据库管理脚本
  
import sys
import os
import commands
import ConfigParser
  
user = 'root'
password = 'root'
defaults_file = '/opt/data/two/my.cnf'
binary_dir = '/opt/mysql/bin'
  
def islive():
    """
        check this server is or isn't running 
    """
    try : 
        config = ConfigParser.ConfigParser()
        config.read( defaults_file )
        pid = config.get( 'mysqld' , 'pid-file' )
        if os.path.exists( pid ):
            return True
        else : 
            return False
    except Exception , e:
        print e 
        sys.exit()
      
      
def status():
    if islive():
        print 'this mysql server is running'
    else :
        print ' this mysql server is stop! '
  
def stop():
    if islive() :
        try :
            config = ConfigParser.ConfigParser()
            config.read( defaults_file )
            socket = config.get( 'mysqld' , 'socket' )
            shell = binary_dir + '/mysqladmin --socket=' + socket + ' -u'+user + ' -p' + password + ' shutdown'
            result = commands.getstatusoutput( shell )
            if result[0] == 0:
                print 'this mysql server is stop successful!'
            else :
                print 'this server is error'
        except Exception ,e:
            print e 
    else :
        print 'this mysql server is already stoped!'
              
  
def start():
    if islive():
        print 'this mysql server is already running'
    else :
        shell = binary_dir + '/mysqld_safe --defaults-file=' + defaults_file + ' &'
        #result = commands.getstatusoutput( shell )
        os.system( shell )
        #if result[0] == 0:
            #print 'this mysql server is start!'
        #else :
            #print 'this server is error'
  
def main():
    try : 
        command = sys.argv[1].strip()
        if command == 'stop':
            stop.__call__()
        elif command == 'start':
            start.__call__()
        elif command == 'restart':
            stop.__call__()
            start.__call__()
        elif command == 'status':
            status.__call__()
        else :
            usage.__call__()
    except:
        usage.__call__()
    else :
        pass
    finally :
        pass
  
def usage():
    print "this script 's usage:\\n",
    print sys.argv[0] + ' start|stop|restart|status '
  
if __name__ == '__main__' :
    main()
#该片段来自于http://www.codesnippet.cn/detail/0408201410110.html
