import socket

HOST = 'time.nist.gov' #podmieniłem serwer na inny, który działą
PORT = 13

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print(data.decode('ascii').strip())
