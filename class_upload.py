# -*- coding:utf-8 -*-
import os
import paramiko
import time
 
class SSHConnection(object):
    
    #项目目录
    projectPath = r'D:/muguangCode/com.mg.web/'
    #项目war目录(war 或 jar 包生成的目录)
    warPath = projectPath + r'target/com.mg.web-0.0.1-SNAPSHOT.war'
    
    def __init__(self, host='139.199.73.14', port=22, username='root',pwd='89n&'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None
 
    def run(self):
        self.connect()  # 连接远程服务器
        #self.package()
        self.upload(self.warPath,'/home/muguang/soft/tomcat8/com.mg.web-0.0.1-SNAPSHOT.war')

        #self.cmd('df')  # 执行df 命令
        self.cmd('sh ./../home/muguang/cc.sh')  # 执行df 命令
        self.close()    # 关闭连接
 
    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

        
    def package(self):
        flag = os.path.exists(self.warPath)
        if flag:
            os.remove(self.warPath)
            print('删除本地旧包----------')        
        os.chdir(self.projectPath)
        os.system('mvn package -Dmaven.test.skip=true -Dspring.active.profile=dev')
        #os.rename(localMkDirPath + createFileName, localMkDirPath + targetFileName)
        print('mvn打包----------')
 
    def upload(self,local_path,target_path):
        time_start=time.time()
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path, target_path, put_call_back)
        time_end=time.time()
        print('totally cost',time_end-time_start)
        
    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        print(result)
        return result


def put_call_back(start, end):
    process = (float(start) / end) * 100
    print("当前上传进度为: %.2f %%" % process)
        
obj = SSHConnection()
obj.run()



    
