#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:54:21 2020

@author: pi
"""

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.IN)

#while True:
#    if GPIO.input(20) == GPIO.HIGH:
#        GPIO.output(2,GPIO.HIGH)
#    else:
#        GPIO.output(2,GPIO.LOW)
#print("Fin de programa")

while True:
    GPIO.output(2,GPIO.inputs(20))
print("Fin de programa")