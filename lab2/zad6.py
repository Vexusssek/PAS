import socket

HOST = '127.0.0.1'
PORT = 2903

l1 = input("Podaj pierwsza liczbe: ")
op = input("Podaj operator (+, -, *, /): ")
l2 = input("Podaj druga liczbe: ")

wiadomosc = f"{l1} {op} {l2}"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(wiadomosc.encode(), (HOST, PORT))
    data, addr = s.recvfrom(1024)
    print("Wynik:", data.decode())
