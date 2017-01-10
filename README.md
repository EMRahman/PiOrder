# PiOrder
Raspberry Pi & Pipsta based restaurant [Point of Sale](https://en.wikipedia.org/wiki/Point_of_sale#Hospitality_industry), [Remote Kitchen Printing](https://www.ecrs.com/products/point-of-sale-pos/remote-kitchen-printing/) &amp; [Online Ordering](https://en.wikipedia.org/wiki/Online_food_ordering).

## Video 
[![IMAGE ALT TEXT HERE](https://github.com/EMRahman/PiOrder/blob/master/Images/youtube.jpeg)](https://www.youtube.com/watch?v=bYomIR-4Y0o)

## Images

###Bar
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image2.JPG)

###Kitchen
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image4.JPG)

###Online Ordering
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1982.PNG)
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1983.PNG)

## Production

Live near Kingswood, Surrey in the UK and fancy a takeout? [Order online!](https://khybertandoori.com/order/login)

NB: Not accessible outside the UK


## Topology
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/Topology.png)

## Features
1. Tablet/touch based POS for waiters.
2. Print bar receipts and tickets to the kitchen. 
3. Online ordering for customers.
4. View the bar or kitchen using RP cameras.

##Technical Overview
   * A Raspberry Pi webserver is used to implement the POS (JavaScript/JQuery/PHP).
   * The Pipsta printers are used to print the customer receipts or kitchen tickets (Python, Bash Scripts, SCP).
   * Orders arriving from a website are sent to the bar and kitchen for printing (SCP).
   * The website creation is agnostic, but we've used Symfony2 & PHP. Bash, Awk and Cron used for handling of the orders and current waiting time.
   * No central database is used - using files is sufficient.

## Hardware
1. 2 x [RP Model 2B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b)
2. 2 x [Pipsta](http://www.pipsta.co.uk)
3. 1 x Web Hosting ([we use 4uhosting.co.uk](https://www.4uhosting.co.uk))
4. 1 x Wifi router & internet connection
5. 1 x Pair of powerline ethernet adaptors
6. 1 (or more) Tablets (for web browsing)
7. Optional: Raspberry Pi Cameras

## FAQ's
Q: Why print onto paper / why not go fully electronic?
A: For customers, a paper receipt is still desired. For chefs, paper has robustness in a kitchen environment. [An interesting discussion here](http://www.cheftalk.com/t/69312/for-those-in-professional-kitchens-ticket-taking-expediting).

Q: How much does this cost?
A: Estimated breakdown below:

| Item            | Cost           | 
| --------------- | --------------:|
|2 Pipsta Printers|           £160|	
|1 Large Tablet   |            £150|
|2 Small Tablets  |            £100|
|1 Printer Cam    |             £20|
|2 Raspberry Pi's |             £70|	
|Powerline Ethernet|	          £50|	
|1 Wireless router|             £30|
|1 Speaker        |             £30|
|Ethernet cables  |              £5|	
|Thermal paper    |        £50/year|
|Web Hosting      |        £65/year|
|Internet & Telephone|    £30/month|

Notes:
* A 3G Mifi costing £30 for the device and £30/year for 12GB is a possibility.
* While a static IP is useful, it isn't strictly necessary.

Q: How reliable are the Pipsta printers, Raspberry Pi's and tablets? 
A: We've been running all the above for a full year with no hardware based problems.

Q: Which tablets are you using?
A: Amazon Kindle Fires (2 x 7 inch and 1 x 10.1 inch)
