#!/usr/bin/env python

import cgi

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
stock4=60
if "hidden" not in form:
	print "<H1>Error: You are not signed in. Click here to go back to </H1>"
	print "<a href="cgi.cs.mcgill.ca/~dandri2/home_stuff.html">Catalogue</a>"
	return 
elif form.getvalue("check1"):
	text1=form.getvalue("text1")
	if text1!=0.0 and stock1!=0:
		print "<p>Item: "
		print "<p>Quantity: ", text1
		price1=10.0
		print "Price: " 
		sum1=text1*price1
		stock1=-text1
	if form.getvalue("check2"):
		text2=form.getvalue("text2")
		if text2 and stock2!=0:
			print "<p>Item: ", 
			print "<p>Quantity: ", text2
			price1=15.0
			print "Price: " 
			sum2=text2*price2
			stock2=-text2
		if form.getvalue("check3"):
			text3=form.getvalue("text3")
			if text3!=0.0  and stock3!=0:
				print "<p>Item: ", 
				print "<p>Quantity: ", text3
				price3=20.0
				print "Price: " 
				sum1=text3*price3 
				stock3=-text3
inventory2=inventory-text1-text2-text3
if inventory2<inventory:
	total=sum1+sum2+sum3
	print "Total: ", total
