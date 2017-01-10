#!/bin/bash

printAtKitchenDir="/tmp/kpos/printAtKitchen"
printAtKitchenProcessedDir="/tmp/kpos/printAtKitchen/processed"
printAtKitchenFailedDir="/tmp/kpos/printAtKitchen/failed"

#Create directories
mkdir -p $printAtKitchenDir
chmod 777 $printAtKitchenDir
mkdir -p $printAtKitchenProcessedDir
chmod 777 $printAtKitchenProcessedDir
mkdir -p $printAtKitchenFailedDir
chmod 777 $printAtKitchenFailedDir

playSoundsForChefs() {
   /usr/bin/omxplayer --no-osd /home/pi/kpos/Roland-R-8-Bell-Tree.wav > /dev/null
   /usr/bin/omxplayer --no-osd /home/pi/kpos/Crash-Cymbal-8.wav > /dev/null
   /usr/bin/omxplayer --no-osd /home/pi/kpos/Alesis-S4-Plus-BrassSect-C3.wav > /dev/null
   /usr/bin/omxplayer --no-osd /home/pi/kpos/Steel-Bell-C6.wav > /dev/null
}

while true
do
	if [ `ls /tmp/kpos/printAtKitchen/*order* 2>/dev/null | wc -l ` -gt 0 ]; then
		for filename in /tmp/kpos/printAtKitchen/*order*; do
			#On success, move to processed directory, on error to failed
			/usr/bin/python /home/pi/kpos/parseAndPrintJobAtKitchen.py $filename $printAtKitchenProcessedDir $printAtKitchenFailedDir
		done
		playSoundsForChefs
        fi

        #Retry failed printing of order at kitchen only
        if [ `ls /tmp/kpos/printAtKitchen/failed/*order* 2>/dev/null | wc -l ` -gt 0 ]; then
                for filename in /tmp/kpos/printAtKitchen/failed/*order*; do
			echo `date` >> /tmp/kpos/filesInError.txt
			echo "File in error detected: $filename" >> /tmp/kpos/filesInError.txt
                        #Print at the kitchen
                        /usr/bin/python /home/pi/kpos/parseAndPrintJobAtKitchen.py $filename $printAtKitchenProcessedDir $printAtKitchenFailedDir
                done
		playSoundsForChefs
        fi

sleep 1 
done
