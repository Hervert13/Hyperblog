#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:32:11 2020

@author: pi
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.IN)

GPIO.output(2,GPIO.LOW)

while True:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(0.00001) #Para mandar pulso de 10ms
    GPIO.output(2,GPIO.LOW)
    time.time()         #Devuelve el numero de segundos desde que el rapsberry se encendio.
    inicio = time.time()
    while GPIO.input(20) == GPIO.LOW:
        inicio = time.time()
    while GPIO.input(20) == GPIO.HIGH:
        fin = time.time()
    rango = fin - inicio
    #2d = rango*34000/s    #Para calcular la distancia, es 2 veces la distancia (ida y vuelta) se elimina los s con los time. 340 m/s ==> 34000/s.
    d = rango*17000
    print("Distancia: ",round(d,1),"cm")
    time.sleep(0.2)