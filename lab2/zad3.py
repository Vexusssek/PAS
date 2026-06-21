import socket

HOST = '127.0.0.1' #podmienione na swerwer lokalny z pliku serwer_lokalny.py
PORT = 2900

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Wpisz wiadomosc (lub 'exit' aby zakonczyc): ")
        if msg.lower() == 'exit':
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        print("Serwer:", data.decode())
