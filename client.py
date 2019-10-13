import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=3000
s.connect(('ip-172-31-46-77.ap-south-1.compute.internal',port))
s.send('Ratan help me'.encode())
print(s.recv(1024))
while True:
        a=input()
        s.send(a.encode())
s.close()

