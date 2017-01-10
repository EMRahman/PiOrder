#!/bin/bash

kpos="/tmp/kpos"
printAtBarDir="/tmp/kpos/printAtBar"
printAtBarProcessedDir="/tmp/kpos/printAtBar/processed"
printAtBarFailedDir="/tmp/kpos/printAtBar/failed"
sendToKitchenDir="/tmp/kpos/sendToKitchen"
sendToKitchenSentDir="/tmp/kpos/sendToKitchen/processed"
sendToKitchenFailedDir="/tmp/kpos/sendToKitchen/failed"
printAtBarForKitchenDir="/tmp/kpos/printAtBarForKitchen/"
printAtBarForKitchenProcessedDir="/tmp/kpos/printAtBarForKitchen/processed"
printAtBarForKitchenFailedDir="/tmp/kpos/printAtBarForKitchen/failed"
printCustomerReceipt="/tmp/kpos/printCustomerReceipt"
printCustomerReceiptProcessedDir="/tmp/kpos/printCustomerReceipt/processed"
printCustomerReceiptFailedDir="/tmp/kpos/printCustomerReceipt/failed"

#Create directories
mkdir -p $kpos
chmod 777 $kpos

mkdir -p $printAtBarDir
chmod 777 $printAtBarDir
mkdir -p $printAtBarProcessedDir
chmod 777 $printAtBarProcessedDir
mkdir -p $printAtBarFailedDir
chmod 777 $printAtBarFailedDir

mkdir -p $sendToKitchenDir
chmod 777 $sendToKitchenDir
mkdir -p $sendToKitchenSentDir
chmod 777 $sendToKitchenSentDir
mkdir -p $sendToKitchenFailedDir
chmod 777 $sendToKitchenFailedDir

mkdir -p $printAtBarForKitchenDir
chmod 777 $printAtBarForKitchenDir
mkdir -p $printAtBarForKitchenProcessedDir
chmod 777 $printAtBarForKitchenProcessedDir
mkdir -p $printAtBarForKitchenFailedDir
chmod 777 $printAtBarForKitchenFailedDir

mkdir -p $printCustomerReceipt
chmod 777 $printCustomerReceipt
mkdir -p $printCustomerReceiptProcessedDir
chmod 777 $printCustomerReceiptProcessedDir
mkdir -p $printCustomerReceiptFailedDir
chmod 777 $printCustomerReceiptFailedDir

while true
do

	if [ `ls -1 /tmp/kpos/sendToKitchen/*order* 2>/dev/null | wc -l ` -gt 0 ]; then
		for filename in /tmp/kpos/sendToKitchen/*order*; do
			#Send to the kitchen
				#Needs finger print check via manually sudo scp-ing
                       		#i.e. sudo -s; scp -i /home/pi/kpos/id_rsa /tmp/test pi@kitchen-printer:/tmp/
			scp -i /home/pi/kpos/id_rsa -o ConnectTimeout=2 $filename pi@kitchen-printer:/tmp/kpos/printAtKitchen/
                        #TODO: print at kitchen if not reachable
			if [ $? -eq 0 ]; then
				mv $filename $sendToKitchenSentDir
                        else
				mv $filename $sendToKitchenFailedDir
			fi
		done
        fi

	if [ `ls /tmp/kpos/printAtBar/*order* 2>/dev/null | wc -l` -gt 0 ]; then
		for filename in /tmp/kpos/printAtBar/*order*; do
			#Print at the bar
                       		#One success, move to processed folder; otherwise failToProcessDir
			/usr/bin/python /home/pi/kpos/parseAndPrintJobAtBar.py $filename $printAtBarProcessedDir $printAtBarFailedDir
		done
        fi

	if [ `ls /tmp/kpos/printAtBarForKitchen/*order* 2>/dev/null | wc -l` -gt 0 ]; then
		for filename in /tmp/kpos/printAtBarForKitchen/*order*; do
			#Print at the bar for kitchen, in event of failing to print at the ktichen
			/usr/bin/python /home/pi/kpos/parseAndPrintJobAtKitchen.py $filename $printAtBarForKitchenProcessedDir $printAtBarForKitchenFailedDir
		done
        fi

	if [ `ls /tmp/kpos/printCustomerReceipt/*order* 2>/dev/null | wc -l` -gt 0 ]; then
		for filename in /tmp/kpos/printCustomerReceipt/*order*; do
			#Print customer receipt, same as the job print but with VAT and logo
			/usr/bin/python /home/pi/kpos/parseAndPrintReceiptAtBar.py $filename $printCustomerReceiptProcessedDir $printCustomerReceiptFailedDir
		done
        fi

	#Retry sending a failed order
	if [ `ls /tmp/kpos/sendToKitchen/failed/*order* 2>/dev/null | wc -l ` -gt 0 ]; then
		for filename in /tmp/kpos/sendToKitchen/failed/*order*; do
			scp -i /home/pi/kpos/id_rsa -o ConnectTimeout=2 $filename pi@kitchen-printer:/tmp/kpos/printAtKitchen/
			if [ $? -eq 0 ]; then
				mv $filename $sendToKitchenSentDir
                        else
				mv $filename $sendToKitchenFailedDir
			fi
		done
        fi

sleep 1 
done
