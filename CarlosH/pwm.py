#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:22:32 2020

@author: pi
"""

#import RPi.GPIO as GPIO
 
#p = GPIO.PWM(#pin, Frecuencia del PWM)  ==> f = 1/T ==> T= 1/f, (f  es en Hz)
#p.start(DC) Ciclo de trabajo ==> DC = 100%*(Ton/T)
#p.ChangeDutyCycle(nuevo_DC) ==> Para cambiar el ciclo de trbajo
#p.stop() ==> para detenerlo

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

pwm = GPIO.PWM(2,500) #T=2ms = 1/500
pwm.start(0)
continuar = True

while continuar:
    a = input("Ingrese el valor del DC: ")
    if a == "f":
        continuar = False
    else:
        dc = int(a)
        pwm.ChangeDutyCycle(dc)
pwm.stop()
print("Fin de programa")
