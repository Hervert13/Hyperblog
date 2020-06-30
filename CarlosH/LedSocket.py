#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:53:58 2020

@author: pi
"""
import socket
import RPi.GPIO as GPIO

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.28.27.28",2019))
s.listen(5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
continuar = True

(sc,addr) = s.accept()
print("Cliente conectado:",addr)

#mensaje = sc.recv(64)
#print("mensaje",mensaje)

while continuar:
    mensaje = sc.recv(64)
    men = str(mensaje)[2:3]
    print("mensaje",men)
    if men =="a":
        GPIO.output(2,GPIO.HIGH)
    elif men =="b":
        GPIO.output(2,GPIO.LOW)
    elif men =="z":
        continuar = False
        
sc.close()
s.close()
print("Fin de programa")