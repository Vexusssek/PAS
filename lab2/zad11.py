import socket

HOST = '127.0.0.1'
PORT = 2908

msg = input("Podaj wiadomosc: ")

if len(msg) < 20:
    msg = msg.ljust(20)
else:
    msg = msg[:20]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode())
    data = s.recv(20)
    print("Odebrano:", data.decode())
