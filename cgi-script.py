#!/usr/bin/env python

import os
import json
import cgi

print "Content-type: text/html"
print
print "<html><body><h1>Hello, world!</h1>"
print "<form method='PUT'><input name='x'></form>"

print "<p>"

form = cgi.FieldStorage()
print "X was: " + cgi.escape(str(form.getvalue("x")))

print "</p>"
print "</body></html>"