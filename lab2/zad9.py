import socket

HOST = '127.0.0.1'
PORT = 2906

ip = input("Podaj adres IP: ")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(ip.encode(), (HOST, PORT))
    data, addr = s.recvfrom(1024)
    print("Hostname:", data.decode())
