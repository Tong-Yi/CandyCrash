#!/usr/bin/python

import cgitb
import cgi
import csv

cgitb.enable()
form=cgi.FieldStorage()
text1=form.getvalue('Quantity1')
text2=form.getvalue('Quantity2')
text3=form.getvalue('Quantity3')

print '''Content-type:text/html\r\n\r\n
<html>
<head>
<title>Bill</title>
</head>
<body>'''
username = form.getfirst("hiddenUser")
if username != "":
        logged = False
        with open('../csv/loggedin.csv','rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar=' ')
            for read in reader:
                if username == read[0]:
                        logged = True
        csvfile.close()

f=open("../csv/inventory.csv","rt")
lines=f.readlines()
stock=[]
for line in lines: 
    row=[]
    items = line.split(",") 
    for item in items:
        row.append(item.strip())
    stock.append(row)
f.close()

quantity=[ 0 for x in range(3)]

name=[]
price=[]
inv = []

for i in range(0,len(stock),1):
    start = stock[i][0]
    main = stock[i][1]
    money = stock[i][2]
    name.append(start)
    price.append(money)
    inv.append(main)
                
price1=float(price[0])
pricee1="%.2f" % price1
price2=float(price[1])
pricee2="%.2f" % price2
price3=float(price[2])
pricee3="%.2f" % price3
stock1=float(stock[0][1])
stock2=float(stock[1][1])
stock3=float(stock[2][1])

if logged == False:
        print '<h2>ERROR'
        print '<h3>You are not signed in. Click here to go back to '
        print '<a href="http://cgi.cs.mcgill.ca/~tyi/catalogue.html">Catalogue</a>'
elif logged == True:
        print '<h2>Bill: </h2>'
        if not(form.getvalue('Lolli')) and not(form.getvalue('M&M')) and not(form.getvalue('Reese')):
                print '<p>No items selected'
        if form.getvalue('Lolli'):      
                quantity[0]=quantity.append(float(text1))     
                if int(text1)>0 and int(text1)<(stock1+1):
                        sum1= price1*int(text1)
                        summ1="%.2f" % sum1
                        stock1-=int(text1)
                        print '<p>Item: ', name[0]
                        print '<p>Quantity: ', text1		
                        print '<p>Price: ', pricee1
                        print '$' 	
                        print '<br><br>'
                elif int(text1)>0 and int(text1)>stock1:
                        summ1=0
                        sums1="%.2f" % summ1
                        print '<p>Item: ', name[0]
                        print '<p>Quantity: Cannot choose a quantity greater than the inventory of ', int(stock1)
                        print '<p>Price: ', pricee1
                        print '$'
                        print '<br><br>'
                elif int(text1)==0:
                        summ1=0
                        sums1="%.2f" % summ1
                        print '<p>Item: ', name[0]
                        print '<p>Quantity: ', text1 
                        print '<p>Price: ', pricee1
                        print '$'
                        print '<br><br>' 
                elif int(text1)<0:
                        summ1=0
                        sums1="%.2f" % summ1
                        print '<p>Item: ', name[0]
                        print '<p>Quantity: Cannot choose a negative quantity.'
                        print '<p>Price: ', pricee1
                        print '$'
                        print '<br><br>' 
        else:
                summ1=0.0

        if form.getvalue('M&M'):
                quantity[1]=quantity.append(float(text2))
                if int(text2)>0 and int(text2)<(stock2+1):
                        sum2=price2*int(text2)
                        summ2="%.2f" % sum2
                        stock2-=int(text2)
                        print '<p>Item: ', name[1]
                        print '<p>Quantity: ', text2          
                        print '<p>Price: ',pricee2 
                        print '$'   
                        print '<br><br>'
                elif int(text2)>0 and int(text2)>stock2:
                        summ2=0
                        sums2="%.2f" % summ2
                        print '<p>Item: ', name[1]
                        print '<p>Quantity: Cannot choose a quantity greater than the inventory of ', int(stock2)
                        print '<p>Price: ', pricee2
                        print '$'
                        print '<br><br>'
                elif int(text2)==0:
                        summ2=0
                        sums2="%.2f" % summ2
                        print '<p>Item: ', name[1]
                        print '<p>Quantity: ', text2
                        print '<p>Price: ', pricee2
                        print '$'
                        print '<br><br>'
                elif int(text2)<0:
                        summ2=0
                        sums2="%.2f" % summ2
                        print '<p>Item: ', name[1]
                        print '<p>Quantity: Cannot choose a negative quantity.'
                        print '<p>Price: ', pricee2
                        print '$'
                        print '<br><br>' 
        else:
                summ2=0.0

        if form.getvalue('Reese'):
                quantity[2]=quantity.append(float(text3))
                if int(text3)>0 and int(text3)<(stock3+1):
                        sum3=price3*int(text3)
                        summ3="%.2f" % sum3
                        stock3-=int(text3)
                        print '<p>Item: ', name[2]
                        print '<p>Quantity: ', text3         
                        print '<p>Price: ',pricee3
                        print '$'   
                        print '<br><br>'
                elif int(text3)>0 and int(text3)>stock3:
                        summ3=0
                        sums3="%.2f" % summ3
                        print '<p>Item: ', name[2]
                        print '<p>Quantity: Cannot choose a quantity greater than the inventory of ', int(stock3)
                        print '<p>Price: ', pricee3
                        print '$'
                        print '<br><br>'
                elif int(text3)==0:
                        summ3=0
                        sums3="%.2f" % summ3
                        print '<p>Item: ', name[2]
                        print '<p>Quantity: ', text3
                        print '<p>Price: ', pricee3
                        print '$'
                        print '<br><br>'
                elif int(text3)<0:
                        summ3=0
                        sums3="%.2f" % summ3
                        print '<p>Item: ', name[2]
                        print '<p>Quantity: Cannot choose a negative quantity.'
                        print '<p>Price: ', pricee3
                        print '$'
                        print '<br><br>' 
        else:
                summ3=0.0

        total=float(summ1)+float(summ2)+float(summ3)
        totall="%.2f" % total

        new = [0 for x in range (3)]
        new[0]=stock1
        new[1]=stock2
        new[2]=stock3
                    
        f2=open("../csv/inventory.csv","w") 
        f2.write("%s,%s,%s\n"%(stock[0][0],new[0],stock[0][2]))
        for index in range(0,2):
            row = index+1
            item = new[index+1]
            update = "%s,%s,%s\n"%(stock[row][0],item,stock[row][2])
            f2.write(update)
        f2.close()

        print '<br><p>Total: ', totall
        print '$'
        print '''<br><br>
        <a href="http://cgi.cs.mcgill.ca/~tyi/index.html">Home</a>
        <a href="http://cgi.cs.mcgill.ca/~tyi/catalogue.html">Catalogue</a>
</body>
</html>'''
