import socket

try:
    socket.inet_pton(socket.AF_INET, input("Podaj adres IP: "))
    print("Poprawny")
except OSError:
    print("Niepoprawny")