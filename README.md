# PiOrder
Raspberry Pi & Pipsta based solution for [Point of Sale](https://en.wikipedia.org/wiki/Point_of_sale#Hospitality_industry), [Remote Kitchen Printing](https://www.ecrs.com/products/point-of-sale-pos/remote-kitchen-printing/) &amp; [Online Ordering](https://en.wikipedia.org/wiki/Online_food_ordering) aimed at restaurants, bars and takeways.

Stats:
- 12,738 in-house & takeout orders printed (Apr 2016 - Nov 2018)
- 1,201 online takeout orders served (Dec 2016 - Nov 2019)
- 235 payments using credit/debit card online (via [Stripe](http://stripe.com/)) (Dec 2016 - Nov 2018)
- 1 [Crypto](http://khybertandoori.com/cryptotill/CryptoTill_CustomerPayment.html) payments (to give perspective, we've just had 1 for a [dine-in customer](https://twitter.com/EhsanRahman/status/967506398081843209)) (Dec 2016 - Nov 2018)
- 0 hardware failures/replacements (Apr 2016 - Nov 2019)

Featured on The MagPi, [May 2017, Issue 57, Page 40.](https://www.raspberrypi.org/magpi-issues/MagPi57.pdf) 

Live example of the online ordering feature: Sadly no longer active (my father, the manager, retired); but you can still order online :) https://khybertandoori.com

## Video 
[![IMAGE ALT TEXT HERE](https://github.com/EMRahman/PiOrder/blob/master/Images/youtube.jpeg)](https://www.youtube.com/watch?v=bYomIR-4Y0o)

## Images

At the Bar:

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image2.JPG)

At the Kitchen:

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image4.JPG)

Online Ordering via an iPhone:

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1982.PNG)
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1983.PNG)

## Production

Sadly no longer active; my father is retired and has passed on the business to new, younger, managers.
NB: Not accessible outside the UK


## Topology
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/Topology.png)

## Features
1. Tablet/touch based POS for waiters.
2. Print bar receipts and tickets to the kitchen. 
3. Online ordering for customers.
4. View the bar or kitchen using RP cameras.

## Technical Overview
   * A Raspberry Pi webserver is used to implement the POS (JavaScript/JQuery/PHP).
   * The Pipsta printers are used to print the customer receipts or kitchen tickets (Python, Bash Scripts, SCP).
   * Orders arriving from a website are sent to the bar and kitchen for printing (SCP).
   * PiOrder is agnostic to the website creation. We've used [Symfony2](https://symfony.com) & PHP. Bash, Awk and Cron used for handling of the orders and current waiting times. [Stripe](http://stripe.com/) used for taking online payments.
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
