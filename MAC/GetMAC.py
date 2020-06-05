# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:06:59 2019

@author: joseluis.mejia
"""
import os

#################################### GET-macadress ###########################################
def getEthName():
  # Get name of the Ethernet interface
  try:
    for root,dirs,files in os.walk('/sys/class/net'):
      for dir in dirs:
        if dir[:3]=='enx' or dir[:3]=='eth':
          interface=dir
  except:
    interface="None"
  return interface


def getMAC(interface='eth0'):    # puede ser wlan0 o eth0 dependiendo de la interfaz a revizar
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]
