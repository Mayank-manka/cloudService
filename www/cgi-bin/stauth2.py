#!/usr/bin/python2
import cgi
import os
import commands
import time

print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dirname=data.getvalue('dname')
dirsize=data.getvalue('dsize')
vg="myhd"

commands.getoutput("lvextend --size +"+dirsize+"M /dev/mapper/"+vg+"-"+dirname)
commands.getoutput("resize2fs /dev/mapper/"+vg+"-"+dirname)
