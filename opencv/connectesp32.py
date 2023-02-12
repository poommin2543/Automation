import socket
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP
s.connect(("192.168.137.224",80))
x = False
y = True
while True:
    y = not y
    s.send(bytes(str(y),'utf-8'))
    # s.send(bytes(str(current_time)+" => PC",'utf-8'))
    data = s.recv(1024)
    print(data.decode())
    time.sleep(1)