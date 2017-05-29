#!/usr/bin/python2
import os
import commands
import time

print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dirname=data.getvalue('dname')
dirsize=data.getvalue('dsize')


commands.getoutput("sudo yum install scsi-target-utils -y")
commands.getoutput("sudo systemctl start nfs-server")
commands.getoutput("sudo systemctl restart tgtd")
vg="myhd"
print commands.getoutput("sudo lvcreate --name "+dirname+" --size "+dirsize+"M "+vg)

iqn="iqn.2003-11.example.com:"+dirname
msg="<target "+iqn+">\nbacking store /dev/myhd/"+dirname+"\n</target>\n"

f=open("/etc/tgt/tgtd.conf",'a+')
f.write(msg)
f.close()

commands.getoutput("sudo iptables -F")
commands.getoutput("sudo setenforce 0")
msg = "#!/usr/bin/python\nimport time,commands\n\ncommands.getoutput('sudo yum install iscsi-initiator-utils -y')\nq=commands.getoutput('sudo iscsiadm --mode discoverydb --type sendtargets --portal 192.168.1.100 --discover')\np=q.split()\ncommands.getoutput('iscsiadm --mode node --targetname "+p[1]+" --portal 192.168.1.100:3260 --login')\ncommands.getoutput('sudo iptables -F')\ncommands.getoutput('sudo setenforce 0')"

f = open("/var/www/html/fblkclient.sh","w")
f.write(msg)
f.close()

web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>STAAS CLOUD</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">STAAS CLOUD</h1>
  <div class="list-group">
    <a href="/fblkclient.sh" class="list-group-item"><b>Download the file and get your block storage</b></a>
    <b>NOTE: AFTER DOWNLOADING THE FILE GIVE IT THE EXECUTION POWER</b>
  </div>
</div>

</body>
</html>
'''

print web
