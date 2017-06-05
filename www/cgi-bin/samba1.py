#!/usr/bin/python2
import cgi
import os
import commands
import time

print "content-type:text/html"
print ""

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
    <h3>Follow the instructions listed:</h3>
    <p>Open <b>RUN</b></p>
    <p>Type -> <b>\\server_ip\drive_name</b></p>
    <p>Click on <b>OK</b></p>
    <p>Enter <b>username</b> and <b>password</b><p>
  </div>
</div>

</body>
</html>
'''

print web
