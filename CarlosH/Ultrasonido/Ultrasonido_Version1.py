#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:32:11 2020

Proyect Estacion de medicion de temperaruta corporal contra COVID-19

@author: pi Carlos Hervert
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)   #Salida Us
GPIO.setup(27,GPIO.OUT)  #Salida Activacion de Medida Termometro
GPIO.setup(20,GPIO.IN)   # Entrada Ultrasonido
GPIO.setup(26,GPIO.IN)   #Entrada Verde
GPIO.setup(4,GPIO.OUT)   #Salida Foco Verde
GPIO.setup(19,GPIO.IN)   #Entrada Rojo
GPIO.setup(13,GPIO.OUT)  #Salida Foco Rojo

GPIO.output(2,GPIO.LOW)

while True:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(0.00001)    #Para mandar pulso de 10ms
    GPIO.output(2,GPIO.LOW)
    time.time()            #Devuelve el numero de segundos desde que el rapsberry se encendio.
    inicio = time.time()
    while GPIO.input(20) == GPIO.LOW:
        inicio = time.time()
    while GPIO.input(20) == GPIO.HIGH:
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
            GPIO.output(27,GPIO.HIGH)
            time.sleep(1.5)
        else:
            GPIO.output(27,GPIO.LOW)
            
    if (GPIO.input(26) == True):        #Se activa foco verde
        
        GPIO.output(4,GPIO.HIGH)
        time.sleep(2.5)
        Lejos = False
        Cerca = False
        GPIO.output(27,GPIO.LOW)
        print("Valor de Verde: ",GPIO.input(26))
        # 1 = Temperatura bien
        # 0 = Temperatura mal
    else:
        GPIO.output(4,GPIO.LOW)
        
    if (GPIO.input(19) == True and GPIO.input(26) == False):      #Se activa foco Rojo
        
        GPIO.output(13,GPIO.HIGH)
        time.sleep(2.5)
        Lejos = False
        Cerca = False
        GPIO.output(27,GPIO.LOW)
        print("Valor de Rojo: ",GPIO.input(19))
    else:
        GPIO.output(13,GPIO.LOW)
        