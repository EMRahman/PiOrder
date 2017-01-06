# PiOrder
Raspberry Pi & Pipsta based EPOS, Restaurant Ticketing &amp; Online Ordering.

##Overview
A Raspberry Pi webserver is used to implement an EPOS (JavaScript/Jquery/PHP).

The Pipsta printers are used to print the customer receipts or kitchen tickets (Python, Bash Scripts, SCP).

Orders arriving from a website are sent to the bar and kitchen for printing (Bash, Awk, SCP).

No central database is used - using files is sufficient for this system.

### Hardware
[RP Model 2B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b)
[Pipsta](http://www.pipsta.co.uk)
Wifi router
Socket ethernet

### Topology
![ScreenShot](https://github.com/EMRahman/PiOrder/blob/master/Topology.png)
