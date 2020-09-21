
#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
Lector y decodificador de ids
"""

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)   #2 Salida Us
GPIO.setup(13,GPIO.OUT)  #27 Salida Activacion de Medida Termometro
GPIO.setup(8,GPIO.IN)   #20 Entrada Ultrasonido Echo
GPIO.setup(37,GPIO.IN)   #26 Entrada Verde
GPIO.setup(7,GPIO.OUT)   #4 Salida Foco Verde
GPIO.setup(35,GPIO.IN)   #19 Entrada Rojo
GPIO.setup(11,GPIO.OUT)  #33 Salida Foco Rojo
GPIO.setup(12,GPIO.OUT)  #13 Led de confirmacion de RFID
GPIO.setup(32,GPIO.OUT)  #led para pantalla

GPIO.output(3,GPIO.LOW)  #Señal de trigger para el Us







GPIO.output(7,GPIO.LOW)  #Apagar Salida Foco Verde
GPIO.output(11,GPIO.LOW) #Apagar Salida Foco Rojo
#GPIO.output(12,GPIO.LOW) #Apagar led de confirmación de RFID


while True:
                #GPIO.output(12,GPIO.HIGH) #Enceder led de confirmacion de RFID
                GPIO.output(3,GPIO.HIGH)
                time.sleep(0.00001)    #Para mandar pulso de 10ms
                GPIO.output(3,GPIO.LOW)
                time.time()            #Devuelve el numero de segundos desde que el rapsberry se encendio.
                inicio = time.time()
                while GPIO.input(8) == GPIO.LOW:
                   inicio = time.time()
                while GPIO.input(8) == GPIO.HIGH:
                    fin = time.time()
                rango = fin - inicio
                #2d = rango*34000/s    #Para calcular la distancia, es 2 veces la distancia (ida y vuelta) se elimina los s con los time. 340 m/s ==> 34000/s.
                d = rango*17000
                print("Distancia: ",round(d,0),"cm")
                time.sleep(0.2)
                GPIO.output(12,GPIO.LOW) #Apagar led de confirmación de RFID

                if d>15.0:                     #Condicional para mandar un solo pulso de medición
                    Lejos = True
                elif d<15.0:
                    Cerca = True
                    if (Lejos == True and Cerca == True):
                        GPIO.output(13,GPIO.HIGH)
                        GPIO.output(32,GPIO.HIGH) #Activa led de pantalla
                        time.sleep(1.5)
                    else:
                        GPIO.output(13,GPIO.LOW)

                if (GPIO.input(37) == True):        #Se activa foco verde

                    GPIO.output(7,GPIO.HIGH)
                    time.sleep(2.5)
                    Lejos = False
                    Cerca = False
                    GPIO.output(13,GPIO.LOW)
                    print("Valor de Verde: ",GPIO.input(37))
                    Read_Us = False
                    estado_temperatura = 1
                    #fecha   = str(datetime.datetime.now())
                    #insert_transactions(cardNumber, employeeNumber, cardHolderName, estado_temperatura, doorId)
                    
                else:
                    GPIO.output(7,GPIO.LOW)


                if (GPIO.input(35) == True and GPIO.input(37) == False):      #Se activa foco Rojo

                    GPIO.output(11,GPIO.HIGH)
                    time.sleep(2.5)
                    Lejos = False
                    Cerca = False
                    GPIO.output(13,GPIO.LOW)
                    print("Valor de Rojo: ",GPIO.input(35))
                    Read_Us = False
                    #estado_temperatura = 0
                    #insert_transactions(cardNumber, employeeNumber, cardHolderName, estado_temperatura, doorId)

                else:
                    GPIO.output(11,GPIO.LOW)
                
                GPIO.output(32,GPIO.LOW) #apagar led de pantalla 
                #signal.signal(signal.SIGINT, end_read)
                #MIFAREReader = MFRC522.MFRC522()


    #except:
     #       print("Error Reader" )
