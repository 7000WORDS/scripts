import socket 

s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host,port))

print("waiting for connection...")
s.listen()


while True:
    conn,addr = s.accept()
    print('Got connection from', addr)
    hi = 'Server saying Hi'
    conn.send(hi.encode())
    conn.close()