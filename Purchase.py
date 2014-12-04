#!/usr/bin/python

import cgi
import webbrowser
form= cgi.FieldStorage()
text1 = 0
text2 = 0
text3 = 0
if  "hidden" not in form:
	webbrowser.open('http://cgi.mcgill.ca')
	sys.exit()

elif form.getvalue('check1'):
	text1=form.getvalue('text1')
	if form.getvalue('check2'):
		text2=form.getvalue('text2')
		if form.getvalue('check3'):
			text3=form.getvalue('text3')
text1 = text1 * 50000
text2 = text2 * 2000
text3 = text3 * 200

