import socket
s=socket.socket()
port=3000
s.bind(('172.31.40.223',port))
s.listen(5)
while True:
        a,b=s.accept()
        print('got connection from ',b)
        #print(a.recv(1024))
        a.send('Ok i will help u '.encode())
        a.close()

