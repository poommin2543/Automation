# import socket
# import time
# from machine import Pin,ADC
# #from time import sleep
# led = Pin(2,Pin.OUT)
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
# s.bind(('',80))
# s.listen(5)
# conn, addr = s.accept()
# 
# while True:
#     data = conn.recv(1024)
#     data = str(data,'utf-8')
#     print(data)
#     if data =="False":
#         led.value(0)
#     elif data =="True":
#         led.value(1)
#         
#     conn.sendall(str(' => ESP','utf-8'))
# 
# conn.close()