# PiOrder
Raspberry Pi & Pipsta based EPOS, Restaurant Ticketing &amp; Online Ordering.

## Images

At the restaurant:

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image2.JPG)

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image3.JPG)

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/image4.JPG)

Mobile ordering:

![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1979.PNG)
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1980.PNG)
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1982.PNG)
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/IMG_1983.PNG)

## Video 
(Video to be completed)

## Live Online Demo

Live near Kingswood, Surrey? [Order online!](https://khybertandoori.com/order/login)
NB: Not accessible outside the UK


### Topology
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Topology.png)

##Features
1. Handling of all orders using a touch based EPOS by waiters. 
   * No manual writing of order
   * No illegibility problems
   * No manual tallying
2. Printing of kitchen tickets at the bar and kitchen: 
   * No carbon copy requiring walking! 
   * We use a camera to physically see the kitchen printouts
   * We play a sound for the chefs to hear the order arrival.
3. View how busy the kitchen is from using other Raspberry Pi cameras. Important for knowing the currentwaiting time for orders.
4. Allow customers to order online:
   * Waiting time can set by waiters via the tablets and/or scheduled. Hangryness should not be underestimated (customers can get very angry if they are hungry and their order is late).
   * Customers order using a webpage. We use [JQuery Mobile](https://jquerymobile.com).
   * Customer can retrieve ast orders, and take their time in ordering.
   * Orders arrive straight to the bar and kitchen printers. 
   * Frees up waiters manually taking a telephone order. 
   * Receipts are emailed to the customers.

##Technical Overview
A Raspberry Pi webserver is used to implement an EPOS (JavaScript/Jquery/PHP).

The Pipsta printers are used to print the customer receipts or kitchen tickets (Python, Bash Scripts, SCP).

Orders arriving from a website are sent to the bar and kitchen for printing (SCP).

The website creation is agnostic, but we've used Symfony2 & PHP. Bash, Awk and Cron used for handling of the orders and current waiting time.

No central database is used - using files is sufficient for this system.

### Hardware
1. 2 x [RP Model 2B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b)
2. 2 x [Pipsta](http://www.pipsta.co.uk)
3. 1 x Web Hosting ([we use 4uhosting.co.uk](https://www.4uhosting.co.uk))
4. 1 x Wifi router & internet connection
5. 1 x Pair of Socket ethernet
6. 1 (or more) Tablets (for web browsing)
7. Optional: Raspberry Pi Cameras
