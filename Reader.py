
#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Lector y decodificador de ids
"""

import RPi.GPIO as GPIO
import MFRC522
import signal
from time import sleep
from MAC.GetMAC import getMAC
from ODBC.conexionDBJL import MSSQL, get_doorId, insert_transactions
from querys.premisys.DML import getQryPeople
import datetime






def qryConsultRFID(cardNumber): 
    conn = MSSQL()
    qryResult = getQryPeople(conn, cardNumber)
#    print(qryResult)
    return qryResult


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


continue_reading    = True
MAC                 = getMAC()
print (MAC)
doorId              = get_doorId(MAC)

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # print ("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
        # print ("invirtiendo el sentido del UID")
        uid3 = []
        uid3 = (hex(uid[3]).split('x')[-1], hex(uid[2]).split('x')[-1], hex(uid[1]).split('x')[-1], hex(uid[0]).split('x')[-1])
        # print ("UID invertido en HEX: ", uid3)

        n = 0
        for i in uid3:
#            print (i)
            if len(i) < 2:
                uid3[n] = (str(0) + str(i))
                # print (".......digito exadecimal corregido", uid3[n])
            n= n + 1
#        print ("los HEX completos son: ",  uid3)

        uuidHEX = (str(uid3[0])+ str(uid3[1])+ str(uid3[2])+ str(uid3[3]))
        uuidDEC = int(uuidHEX, 16)
        # print ("UUID en la BD debe ser: ", uuidDEC)
        
        qryResult = qryConsultRFID(str(uuidDEC))
        try:
            cardNumber = str(qryResult[1][2])
            employeeNumber = str(qryResult[1][1])
            if employeeNumber == "None":
                employeeNumber = " "
            cardHolderName = str(qryResult[1][0])
        
        except:
            print("no se encontró tarjeta en premisis")
        
        insert_transactions(cardNumber, employeeNumber, cardHolderName, doorId)
        fecha   = str(datetime.datetime.now()) 
        print(fecha, employeeNumber, cardHolderName)