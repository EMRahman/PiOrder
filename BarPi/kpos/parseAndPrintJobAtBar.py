#!/bin/python
import sys  
import socket
from xml.dom import minidom
import time
import subprocess
import barPrint
import shutil
import imagePrint
import datetime

#Read argument of what should be printed via this printer
if len(sys.argv) <3:
	print "Usage: parseAndPrintJobAtBar.py <file to print> <dir on success> <dir on failure>"
        sys.exit(1)

jobToPrint = sys.argv[1]
dirOnSuccess = sys.argv[2]
dirOnFailure = sys.argv[3]

xmlToProcess = open(jobToPrint)
xmlToProcess = xmlToProcess.read()
xmldoc = minidom.parseString(xmlToProcess)

#Get footer text
footerText=''
with open ("/home/pi/kpos/footer.txt", "r") as myfile:
    footerText=myfile.read()

orderString = ''
takeoutOrInhouse = xmldoc.getElementsByTagName('takeoutOrInhouse')[0].firstChild.nodeValue
if(takeoutOrInhouse == 'TAKEOUT'):
	customer = xmldoc.getElementsByTagName('customer')[0].firstChild.nodeValue
	orderTime = xmldoc.getElementsByTagName('orderTime')[0].firstChild.nodeValue
	collectionTime = xmldoc.getElementsByTagName('collectionTime')[0].firstChild.nodeValue
	orderString += "Customer: "+ customer +"\n"
	orderString += "Time Ordered: "+ orderTime +"\n"
	orderString += "Collection Time: "+ collectionTime +"\n"
else:
	tableNumber = xmldoc.getElementsByTagName('tableNumber')[0].firstChild.nodeValue
	numbOfCust = xmldoc.getElementsByTagName('numbOfCust')[0].firstChild.nodeValue	
	printTime = xmldoc.getElementsByTagName('printTime')[0].firstChild.nodeValue	
	orderString += "Table Number: "+ tableNumber +"\n"
	orderString += "No. of Customers: "+ numbOfCust +"\n"
	orderString += "Print Time: "+ printTime +"\n"

timestamp = xmldoc.getElementsByTagName('timestamp')[0].firstChild.nodeValue
timestamp_date = datetime.datetime.fromtimestamp(int(timestamp[0:10])).strftime('%a %d %b %Y')
orderString += "Date: " +timestamp_date +"\n"

if len(xmldoc.getElementsByTagName('standingOrder'))==1:
        orderString += 'STANDING ORDER\n'
orderNote = ''
if len(xmldoc.getElementsByTagName('orderNote'))==1:
        orderNote = xmldoc.getElementsByTagName('orderNote')[0].firstChild.nodeValue
        orderString += 'Order Note:' + orderNote + '\n\n'
itemlist = xmldoc.getElementsByTagName('item')
prevCategory=''
chutenyChargePrinted=False
for s in itemlist:
	category = s.getElementsByTagName('category')[0].firstChild.nodeValue
        if (category!=prevCategory):
                print prevCategory
                orderString += "\n" + category + "\n"
                prevCategory = category
        if (takeoutOrInhouse == 'INHOUSE' and category=="Popadoms" and chutenyChargePrinted==False):
                chutneysCharge = xmldoc.getElementsByTagName('chutneysCharge')[0].firstChild.nodeValue
                padding = 30 - len("Chutneys" + chutneysCharge)
                orderString += "Chutneys" + " "*padding + chutneysCharge+ "\n"
                chutenyChargePrinted = True
	qty = s.getElementsByTagName('qty')[0].firstChild.nodeValue
	foodDesc= s.getElementsByTagName('foodDesc')[0].firstChild.nodeValue
	subTotal = s.getElementsByTagName('subtotal')[0].firstChild.nodeValue
	textLength = len(qty + " " + foodDesc + " " + subTotal)
	if (textLength > 30):
		orderString += qty + " " + foodDesc + "\n"
		padding = 30 - len(subTotal)
		orderString += " "*padding + subTotal + "\n"
	else:
		padding = 30 - len(qty + " " + foodDesc + " " + subTotal)
		orderString += qty + " " + foodDesc + " " +" "*padding + subTotal +"\n"

totQty = xmldoc.getElementsByTagName('totalQty')[0].firstChild.nodeValue
serviceCharge = xmldoc.getElementsByTagName('serviceCharge')[0].firstChild.nodeValue
totalCost= xmldoc.getElementsByTagName('total')[0].firstChild.nodeValue

padding = 30 - len("Total Qty: " + totQty)
orderString += "\nTotal Qty: " + " "*padding + totQty + "\n"
if (takeoutOrInhouse == 'INHOUSE'):
        padding = 30 - len("Service: " + serviceCharge)
        orderString += "Service: " + " "*padding + serviceCharge+"\n"
padding = 30 - len("Total Cost: " + totalCost)
orderString += "Total Cost: " + " "*padding + totalCost +"\n"
orderString += "\n"+footerText

#Printing to the printer goes here

#For Testing: Print the string to file
#tmpFile = open('/tmp/toPrint.o','w')
#tmpFile.write(orderString)
#tmpFile.close()

#For testing: Print the output to stdout
#print orderString

#Print to the printer
try:
        barPrint.printToPrinter(orderString)
        shutil.move(jobToPrint,dirOnSuccess)
except:
        shutil.move(jobToPrint,dirOnFailure)
        raise
