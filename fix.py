#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:06:10 2020

@author: pi
"""
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

uid = [227, 92, 12, 222, 109]
uid3 = []
uid3 = (hex(uid[3]).split('x')[-1], hex(uid[2]).split('x')[-1], hex(uid[1]).split('x')[-1], hex(uid[0]).split('x')[-1])
# print ("UID invertido en HEX: ", uid3)

n = 0
for i in uid3:
    print (i)
    if len(i) < 2:
        uid3[n] = (str(0) + str(i))
        # print (".......digito exadecimal corregido", uid3[n])
    n= n + 1
#        print ("los HEX completos son: ",  uid3)

uuidHEX = (str(uid3[0])+ str(uid3[1])+ str(uid3[2])+ str(uid3[3]))
uuidDEC = int(uuidHEX, 16)
# print ("UUID en la BD debe ser: ", uuidDEC)

qryResult = qryConsultRFID(str(uuidDEC))
