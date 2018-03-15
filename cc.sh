#!/bin/bash
tomcat_home="/home/muguang/soft/tomcat8"
file1="${tomcat_home}/com.mg.web-0.0.1-SNAPSHOT.war"
file2="${tomcat_home}/com.mg.backgroud-0.0.1-SNAPSHOT.war"
SHUTDOWN=$tomcat_home/bin/shutdown.sh  
STARTTOMCAT=$tomcat_home/bin/startup.sh

echo "关闭$tomcat_home" 
$SHUTDOWN
#ps -ef |grep tomcat |grep $tomcat_home |grep -v 'grep'|awk '{print $2}' | xargs kill -9
pidlist=`ps -ef |grep tomcat  |grep -v "grep"|awk '{print $2}'`   
kill -9 $pidlist  
if [ -f "$file1" ]
then
 echo "$file1 doing........"
 rm -rf ${tomcat_home}/webapps/muguangsys.war
 rm -rf ${tomcat_home}/webapps/muguangsys
 mv $file1 ${tomcat_home}/webapps/muguangsys.war
else
 echo "$file1 not found."
fi

if [ -f "$file2" ]
then
 echo "$file2 doing........"
 rm -rf ${tomcat_home}/webapps/bg.war
 rm -rf ${tomcat_home}/webapps/bg
 mv $file2 ${tomcat_home}/webapps/bg.war
else
 echo "$file2 not found."
fi

sleep 5
echo "开启$tomcat_home" 
$STARTTOMCAT  


