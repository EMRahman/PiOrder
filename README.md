# PiOrder
Raspberry Pi & Pipsta based restaurant [Point of Sale](https://en.wikipedia.org/wiki/Point_of_sale#Hospitality_industry), Ticketing &amp; Online Ordering.

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
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Images/Topology.png)

##Features
1. Handling of all orders using a touch based EPOS by waiters. 
   * No manual writing of orders
   * No illegibility problems
   * No manual tallying with a calculator
2. Printing of kitchen tickets at the bar and kitchen: 
   * No carbon paper copy requiring walking to the kitchen! 
   * We use a camera to physically see the kitchen printouts
   * We play a sound for the chefs to hear the order arrival.
3. View how busy the kitchen is from using other Raspberry Pi cameras. Important for knowing the current waiting time for orders.
4. Allow customers to order online:
   * Frees up waiters manually taking a telephone order. 
   * Waiting time can set by waiters via the tablets and/or scheduled; so the customer is informed how long their order will take.
   * Customers order using a webpage. We use [JQuery Mobile](https://jquerymobile.com).
   * Customers can easily reload previous orders and take their time in ordering.
   * Orders arrive straight to the bar and kitchen printers. Optional order review page and safety valves placed for security. 
   * Receipts are emailed to the customers.

##Technical Overview
   * A Raspberry Pi webserver is used to implement the POS (JavaScript/JQuery/PHP).
   * The Pipsta printers are used to print the customer receipts or kitchen tickets (Python, Bash Scripts, SCP).
   * Orders arriving from a website are sent to the bar and kitchen for printing (SCP).
   * The website creation is agnostic, but we've used Symfony2 & PHP. Bash, Awk and Cron used for handling of the orders and current waiting time.
   * No central database is used - using files is sufficient.

### Hardware
1. 2 x [RP Model 2B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b)
2. 2 x [Pipsta](http://www.pipsta.co.uk)
3. 1 x Web Hosting ([we use 4uhosting.co.uk](https://www.4uhosting.co.uk))
4. 1 x Wifi router & internet connection
5. 1 x Pair of powerline ethernet adaptors
6. 1 (or more) Tablets (for web browsing)
7. Optional: Raspberry Pi Cameras

#FAQ's
Q: Why print onto paper / why not go fully electronic?

A: For customers, a paper receipt is still common. For chefs in the kitchen, paper has value in a kitchen environment. [An interesting discussion here](http://www.cheftalk.com/t/69312/for-those-in-professional-kitchens-ticket-taking-expediting).

Q: How much does this cost roughly?

A: Approx £545 for the hardware, then £45/year for Web Hosting and £30/month for Telehphone & Internet. The internet can of course be shared with customers as a service.

Breakdown:
1 Large Tablet £130	
2 Small Tablets £100	
Wireless router £30	
Printer Cam £20	
2 Raspberry Pi's £70	
2 Printers £140	
Socket Ethernet 	£50	
Ethernet cables £5	
Web Hosting £45/Per Year
Monthly Internet £30/Month (includes telephone service)

Q: Why not just use EposNow?

A: A) EposNow offer £1,119 for a standalone system alone; with no online ordering capability.

Q: Why not just use JustEat?

A: A) It's just for online ordering and B) It's expensive! It's (at the time of writing £838.8) to just sign-up and the average monthly cost is ~£500. The above setup cost is 
* [Article 1](http://www.managementtoday.co.uk/dont-eat-two-thirds-takeaways-say-just-eats-fees-unfair/article/1299038)
* [Article 2](https://www.preoday.com/blog/just-eat-really-best-option-takeaway/)
* [JustEat Official Costs](https://restaurants.just-eat.co.uk/benefits.html)
