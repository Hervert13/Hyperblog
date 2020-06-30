#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:16:56 2020

@author: pi
"""
#import RPI.GPIO as GPIO

#funcion para trabajar con los pines
#GPIO.setmode(modo)
        #GPIO.setmode(GPIO.BOARD)    ==> FORMATO BOARD
        #GPIO.setmode(GPIO.BCM)      ==> fORMATO GPIO

#Configuracion de pines
#GPIO.setup(#pin,GPIO.OUT)    ==> salida
#GPIO.setup(#pin,GPIO.IN)    ==> entrada

#Funciones cuando un pin es configurado como salida
#GPIO.otput(#pin,valor)
        #GPIO.output(#pin,GPIO.HIGH)
        #GPIO.output(#pin,1)
        #GPIO.ouput(#pin,GPIO.LOW)
        #GPIO.output(#pin,0)
        
#Funcion que tenekos enmodo entrada
#GPIO.input(#pin)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.OUT)

continuar = True
while continuar:
    a = input("Digite una letra: ")
    if a=="a":
        GPIO.output(27,GPIO.HIGH)
    elif a=="b":
        GPIO.output(27,GPIO.LOW)
    elif a=="z":
        continuar = False
print("Fin de programa")

