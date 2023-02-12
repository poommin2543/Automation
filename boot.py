# try:
#   import usocket as socket
# except:
#   import socket
# 
# from machine import Pin
# import network
# 
# import esp
# esp.osdebug(None)
# 
# import gc
# gc.collect()
# 
# #ssid = 'KunLalit'
# #password = '12345678'
# ssid = 'NNN2281'
# password = '12345678P'
# 
# station = network.WLAN(network.STA_IF)
# 
# station.active(True)
# station.connect(ssid, password)
# 
# while station.isconnected() == False:
#   pass
# 
# print('Connection successful')
# print(station.ifconfig())
# 
# led = Pin(2, Pin.OUT)
# 