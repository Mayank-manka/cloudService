#!/usr/bin/python2
import cgi
import os
import commands
import time

print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dirname=data.getvalue('dname')
dirram=data.getvalue('dram')
dircpu=data.getvalue('dcpu')
print "1111"
os.system('yum install virt-install -y')
print "2222"
print os.system('virt-install --cdrom /root/Downloads/ubuntu-14.04-desktop-amd64.iso --ram '+dirram+' --vcpu '+dircpu+' --nodisk --name '+dirname+' --graphics vnc,port=5910,listen=0.0.0.0')
os.system('yum install novnc python-sockify -y')
os.system('websockify --web=/usr/share/novnc 6080 192.168.1.100:5912')

web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>IAAS CLOUD</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">IAAS CLOUD</h1>
  <div class="list-group">
    <a href="/cli.sh" class="list-group-item"><b>Download the file and launch your OS</b></a>
  </div>
</div>

</body>
</html>
'''

print web
