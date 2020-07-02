#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:46:48 2020

@author: pi
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

while True:
    GPIO.output(2,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(2,GPIO.LOW)
    time.sleep(2)
    
print("Fin del programa")