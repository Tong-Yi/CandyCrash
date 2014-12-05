#!/usr/bin/python

import cgi
<<<<<<< HEAD
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
=======

form=cgi.FieldStorage()
text1=0
text2=0
text3=0
sum1=0.0
sum2=0.0
sum3=0.0
total=0.0
stock1=100
stock2=50
stock3=25
total=0.0
if "hidden" not in form:
	print "ERROR"
	print "You are not signed in. Click here to go back to "
	print "<a href="http://cgi.cs.mcgill.ca/~dandri2/catalogue.html">Catalogue</a>"
	return 
elif form.getvalue('check1'):
	print "Bill: "
	text1=form.getvalue('text1')
	if text1!=0 and stock1!=0 and text1<(stock1+1):
		print "<p>Item: Lollipop"
		print "<p>Quantity: ", text1
		price1=10.00
		print "Price: " 
		sum1=text1*price1
		stock1=-text1
	if form.getvalue('check2'):
		text2=form.getvalue('text2')
		if text2!=0 and stock2!=0 and text2<(stock2+1):
			print "<p>Item: M&M's", 
			print "<p>Quantity: ", text2
			price2=15.00
			print "Price: " 
			sum2=text2*price2
			stock2=-text2
	if form.getvalue('check3'):
		text3=form.getvalue('text3')
		if text3!=0 and stock3!=0 and text3<(stock3+1):
			print "<p>Item: Reese Chocolate", 
			print "<p>Quantity: ", text3
			price3=20.00
			print "Price: " 
			sum3=text3*price3 
			stock3=-text3
	total=sum1+sum2+sum3
	print "Total: ", total
	print "<a href="http://cgi.cs.mcgill.ca/~dandri2/catalogue.html">Catalogue</a>"
	print "<a href="http://cgi.cs.mcgill.ca/~nboukh5/index.html">Catalogue</a>"
>>>>>>> 692e248302b5e6dd88d4f05bd725fa1cc617ac67

