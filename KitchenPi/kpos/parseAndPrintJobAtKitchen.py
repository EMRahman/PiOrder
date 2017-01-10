#!/bin/python
import sys  
import socket
from xml.dom import minidom
import time
import subprocess
import kitchenPrint
import shutil

#Read argument of what should be printed via this printer
if len(sys.argv) <3:
	print "Usage: parseAndPrintJobAtKitchen.py <file to print> <dir on success> <dir on failure>"
        sys.exit(1)

jobToPrint = sys.argv[1]
dirOnSuccess = sys.argv[2]
dirOnFailure = sys.argv[3]

xmlToProcess = open(jobToPrint)
xmlToProcess = xmlToProcess.read()
xmldoc = minidom.parseString(xmlToProcess)

orderString = '\n\n'
takeoutOrInhouse = xmldoc.getElementsByTagName('takeoutOrInhouse')[0].firstChild.nodeValue
if(takeoutOrInhouse == 'TAKEOUT'):
        customer = xmldoc.getElementsByTagName('customer')[0].firstChild.nodeValue
        orderTime = xmldoc.getElementsByTagName('orderTime')[0].firstChild.nodeValue
        collectionTime = xmldoc.getElementsByTagName('collectionTime')[0].firstChild.nodeValue
        orderString += "Customer: "+ customer +"\n"
        orderString += '    TAKEOUT\n'
else:
        tableNumber = xmldoc.getElementsByTagName('tableNumber')[0].firstChild.nodeValue
        numbOfCust = xmldoc.getElementsByTagName('numbOfCust')[0].firstChild.nodeValue
        printTime = xmldoc.getElementsByTagName('printTime')[0].firstChild.nodeValue
        inhouseReadyTime = xmldoc.getElementsByTagName('inhouseReadyTime')[0].firstChild.nodeValue
        orderString += "Table  "+ tableNumber +"\n"
        orderString += "Customers: "+ numbOfCust +"\n"
        orderString += "Ordered: "+ printTime +"\n"
        orderString += '****************\n'
        orderString += '    INHOUSE\n'
        orderString += '****************\n'

if len(xmldoc.getElementsByTagName('standingOrder'))==1:
	orderString += '@STANDING ORDER@\n\n'
orderNote = ''
if len(xmldoc.getElementsByTagName('orderNote'))==1:
	orderNote = xmldoc.getElementsByTagName('orderNote')[0].firstChild.nodeValue
	orderString += 'NOTE:' + orderNote + '\n'

itemlist = xmldoc.getElementsByTagName('item')
#orderString += "\n"
prevCategory=''
for s in itemlist:
	category = s.getElementsByTagName('category')[0].firstChild.nodeValue
	if(takeoutOrInhouse == 'INHOUSE'):
		if(category=='Popadoms'):
			continue
		if(category=='Drinks'):
			continue
	if(category!='Starters' and prevCategory=='Starters'):
		orderString += "----------------\n\n"
#TODO: if onyl starters then there will be no line. Unlikely.
	if(category!=prevCategory):
		orderString += "\n"
	prevCategory = category
	qty = s.getElementsByTagName('qty')[0].firstChild.nodeValue
	foodDesc= s.getElementsByTagName('outDescrip')[0].firstChild.nodeValue
	orderString += qty + " " + foodDesc.upper() + "\n"

#print strftime("%Y-%m-%d %H:%M:%S") + " Printing the following: \n" + orderString
#orderString += "\n\nCollection: "+ collectionTime
if(takeoutOrInhouse == 'TAKEOUT'):
        orderString += "\n     "+ collectionTime + "\n"
else:
        orderString += "\n     "+ inhouseReadyTime + "\n"
        orderString += '\n'
        orderString += '****************\n'
        orderString += '    INHOUSE\n'
        orderString += '****************\n'

#Printing to the printer goes here

#For Testing: Print the string to file
#tmpFile = open('/tmp/toPrint.o','w')
#tmpFile.write(orderString)
#tmpFile.close()

#For testing: Print the output to stdout
#print orderString
#print "MAIN CHEF\n" + orderString + "\n"
#print "TANDOORI CHEF\n" + orderString + "\n"

#Print to the printer
try:
        orderString_main = "MAIN CHEF\n" + orderString + "\n"
        orderString_tandChef = "TANDOORI CHEF\n" + orderString + "\n"
        kitchenPrint.printToPrinter(orderString_main)
        time.sleep(5)
        kitchenPrint.printToPrinter(orderString_tandChef)
        time.sleep(5)
        shutil.move(jobToPrint,dirOnSuccess)
except:
        shutil.move(jobToPrint,dirOnFailure)
        raise
