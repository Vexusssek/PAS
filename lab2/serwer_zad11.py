import socket

HOST = '127.0.0.1'
PORT = 2908

wiadomosc = input("Wpisz wiadomosc do wyslania: ")

wiadomosc_20 = wiadomosc[:20].ljust(20, ' ')

print(f"Wysyłam pakiet (długość {len(wiadomosc_20)}): '{wiadomosc_20}'")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(wiadomosc_20.encode('utf-8'))

    data = s.recv(20)
    print(
        f"Odebrano od serwera (długość {len(data)}): '{data.decode('utf-8')}'"
    )