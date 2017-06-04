#!/usr/bin/python2
import cgi,commands,time
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
a=data.getvalue('id11')
b=data.getvalue('id12')

commands.getoutput("sudo aws ec2 attach-volume --volume-id "+a+" --instance-id "+b+" --device /dev/sdf")


web='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>AMAZON AWS</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/template1.css">
  <script src="/static/template2.js"></script>
  <script src="/static/template3.js"></script>
</head>
<body style="background-color:powderblue">
<div class="container">
  <h1 style="color:red">AMAZON AWS</h1>
  <div class="list-group">
   <h3>VOLUME ATTACHED</h3>
  </div>
</div>

</body>
</html>
'''

print web
