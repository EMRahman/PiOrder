import argparse
import platform
import sys
import time

import usb.core
import usb.util

FEED_PAST_CUTTER = b'\n' * 5
NEWLINE = b'\n'
USB_BUSY = 66

# NOTE: The following section establishes communication to the Pipsta printer
# via USB. YOU DO NOT NEED TO UNDERSTAND THIS SECTION TO PROGRESS WITH THE
# TUTORIALS! ALTERING THIS SECTION IN ANY WAY CAN CAUSE A FAILURE TO COMMUNICATE
# WITH THE PIPSTA. If you are interested in learning about what is happening
# herein, please look at the following references:
#
# PyUSB: http://sourceforge.net/apps/trac/pyusb/
# ...which is a wrapper for...
# LibUSB: http://www.libusb.org/
#
# For full help on PyUSB, at the IDLE prompt, type:
# >>> import usb
# >>> help(usb)
# 'Deeper' help can be trawled by (e.g.):
# >>> help(usb.core)
#
# or at the Linux prompt, type:
# pydoc usb
# pydoc usb.core
PIPSTA_USB_VENDOR_ID = 0x0483
PIPSTA_USB_PRODUCT_ID = 0xA053

def printToPrinter(text):
    if platform.system() != 'Linux':
        sys.exit('This script has only been written for Linux')

    # Find the Pipsta's specific Vendor ID and Product ID
    dev = usb.core.find(idVendor=PIPSTA_USB_VENDOR_ID,
                        idProduct=PIPSTA_USB_PRODUCT_ID)
    if dev is None:  # if no such device is connected...
        raise IOError('Printer  not found')  # ...report error

    try:
        # Linux requires USB devices to be reset before configuring, may not be
        # required on other operating systems.
        dev.reset()

        # Initialisation. Passing no arguments sets the configuration to the
        # currently active configuration.
        dev.set_configuration()
    except usb.core.USBError as ex:
        raise IOError('Failed to configure the printer', ex)

    # The following steps get an 'Endpoint instance'. It uses
    # PyUSB's versatile find_descriptor functionality to claim
    # the interface and get a handle to the endpoint
    # An introduction to this (forming the basis of the code below)
    # can be found at:

    cfg = dev.get_active_configuration()  # Get a handle to the active interface

    interface_number = cfg[(0, 0)].bInterfaceNumber
    # added to silence Linux complaint about unclaimed interface, it should be
    # release automatically
    usb.util.claim_interface(dev, interface_number)
    alternate_setting = usb.control.get_interface(dev, interface_number)
    interface = usb.util.find_descriptor(
        cfg, bInterfaceNumber=interface_number,
        bAlternateSetting=alternate_setting)

    usb_endpoint = usb.util.find_descriptor(
        interface,
        custom_match=lambda e:
        usb.util.endpoint_direction(e.bEndpointAddress) ==
        usb.util.ENDPOINT_OUT
    )

    if usb_endpoint is None:  # check we have a real endpoint handle
        raise IOError("Could not find an endpoint to print to")

    # Now that the USB endpoint is open, we can start to send data to the
    # printer.
    # The following opens the text_file, by using the 'with' statemnent there is
    # no need to close the text_file manually.  This method ensures that the
    # close is called in all situation (including unhandled exceptions).
    
    #usb_endpoint.write(b'\x1b!\x80')
    #usb_endpoint.write("Khyber Tandoori")
    #usb_endpoint.write("KHYBER TANDOORI RESTAURANT")
    #usb_endpoint.write(NEWLINE)
    #usb_endpoint.write(b'\x1b!\x00')
    usb_endpoint.write(b'\x1b!\x20')
    usb_endpoint.write(NEWLINE)
    usb_endpoint.write(NEWLINE)
    usb_endpoint.write(NEWLINE)

    # Print a char at a time and check the printers buffer isn't full
    for x in text:
    #for x in sys.stdin:
        usb_endpoint.write(x)    # write all the data to the USB OUT endpoint
        
        res = dev.ctrl_transfer(0xC0, 0x0E, 0x020E, 0, 2)
        while res[0] == USB_BUSY:
            time.sleep(0.01)
            res = dev.ctrl_transfer(0xC0, 0x0E, 0x020E, 0, 2)
    
    #from time import strftime
    #timeNow=strftime("%a %d-%b-%Y %H:%M:%S")    
    #usb_endpoint.write(timeNow)
    usb_endpoint.write(FEED_PAST_CUTTER)
    usb.util.dispose_resources(dev)
