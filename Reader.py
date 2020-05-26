
#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Lector y decodificador de ids
"""

import RPi.GPIO as GPIO
import MFRC522
import signal
from time import sleep


continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
        print "invirtiendo el sentido del UID"
        uid2 = []
        uid3 = []

        uid2 = (uid[3], uid[2], uid[1], uid[0])
        print "UID invertido: ", uid2

        uid3 = (hex(uid[3]).split('x')[-1], hex(uid[2]).split('x')[-1], hex(uid[1]).split('x')[-1], hex(uid[0]).split('x')[-1])
        print "UID invertido en HEX: ", uid2
        sleep (3)

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]


        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)


        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

#        print("pause")
#        sleep(5)


        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(11)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"
