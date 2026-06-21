import socket

HOST = '127.0.0.1'
PORT = 2902

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        msg = input("Wpisz wiadomosc (lub 'exit' aby zakonczyc): ")
        if msg.lower() == 'exit':
            break
        s.sendto(msg.encode(), (HOST, PORT))
        data, addr = s.recvfrom(1024)
        print("Serwer:", data.decode())
