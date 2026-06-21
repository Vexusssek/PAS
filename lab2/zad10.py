import socket

HOST = '127.0.0.1'
PORT = 2907

hostname = input("Podaj nazwe hostname: ")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(hostname.encode(), (HOST, PORT))
    data, addr = s.recvfrom(1024)
    print("Adres IP:", data.decode())
