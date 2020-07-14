
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
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)   #2 Salida Us
GPIO.setup(13,GPIO.OUT)  #27 Salida Activacion de Medida Termometro
GPIO.setup(38,GPIO.IN)   #20 Entrada Ultrasonido
GPIO.setup(37,GPIO.IN)   #26 Entrada Verde
GPIO.setup(7,GPIO.OUT)   #4 Salida Foco Verde
GPIO.setup(35,GPIO.IN)   #19 Entrada Rojo
GPIO.setup(33,GPIO.OUT)  #13 Salida Foco Rojo

GPIO.output(3,GPIO.LOW)  #Señal de trigger para el Us



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

Read_Us             = False
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
    GPIO.output(7,GPIO.LOW)
    GPIO.output(33,GPIO.LOW)
    
    try:
        # Scan for cards
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        # if status == MIFAREReader.MI_OK:
        #     print ("Card detected")
    
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
    
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            print ("Prueba: ", status)
            Read_Us = True 
    
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
                fecha   = str(datetime.datetime.now())
                print(fecha, "No se encontró tarjeta en premisis", uuidDEC)
                
            insert_transactions(cardNumber, employeeNumber, cardHolderName, doorId)
            fecha   = str(datetime.datetime.now())
            print("Card detected ", fecha, employeeNumber, cardHolderName)
            sleep(1.5)
            
        while Read_Us:
            GPIO.output(3,GPIO.HIGH)
            time.sleep(0.00001)    #Para mandar pulso de 10ms
            GPIO.output(3,GPIO.LOW)
            time.time()            #Devuelve el numero de segundos desde que el rapsberry se encendio.
            inicio = time.time()
            while GPIO.input(38) == GPIO.LOW:
               inicio = time.time()
            while GPIO.input(38) == GPIO.HIGH:
                fin = time.time()
            rango = fin - inicio
            #2d = rango*34000/s    #Para calcular la distancia, es 2 veces la distancia (ida y vuelta) se elimina los s con los time. 340 m/s ==> 34000/s.
            d = rango*17000
            print("Distancia: ",round(d,0),"cm")
            time.sleep(0.2)
    
            if d>15.0:                     #Condicional para mandar un solo pulso de medición
                Lejos = True
            elif d<15.0:
                Cerca = True
                if (Lejos == True and Cerca == True):                       
                    GPIO.output(13,GPIO.HIGH)
                    time.sleep(1.5)
                else:
                    GPIO.output(13,GPIO.LOW)
            
            if (GPIO.input(37) == True):        #Se activa foco verde
        
                GPIO.output(7,GPIO.HIGH)
                time.sleep(3.5)
                Lejos = False
                Cerca = False
                GPIO.output(13,GPIO.LOW)
                print("Valor de Verde: ",GPIO.input(37))
                Read_Us = False
                #continue_reading    = True
                # 1 = Temperatura bien
                # 0 = Temperatura mal
            else:
                GPIO.output(7,GPIO.LOW)
                
        
            if (GPIO.input(35) == True and GPIO.input(37) == False):      #Se activa foco Rojo
        
                GPIO.output(33,GPIO.HIGH)
                time.sleep(3.5)
                Lejos = False
                Cerca = False
                GPIO.output(13,GPIO.LOW)
                print("Valor de Rojo: ",GPIO.input(35))
                Read_Us = False
                #continue_reading    = True
            else:
                GPIO.output(33,GPIO.LOW)            
            
    except:
            print("Error" )