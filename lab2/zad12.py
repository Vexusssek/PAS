import socket

HOST = '127.0.0.1'
PORT = 2908

msg = input("Podaj wiadomosc: ")

if len(msg) < 20:
    msg = msg.ljust(20)
else:
    msg = msg[:20]


def odbierz_dokladnie(sock, rozmiar):
    bufor = b''
    while len(bufor) < rozmiar:
        brakujace = rozmiar - len(bufor)
        paczka = sock.recv(brakujace)

        if not paczka:
            raise ConnectionError(
                f"Połączenie zamknięte przed odebraniem całego pakietu. Posiadane dane: {len(bufor)}/{rozmiar}"
            )

        bufor += paczka
    return bufor


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode())

    try:
        surowe_dane = odbierz_dokladnie(s, 20)
        print("Odebrano pomyślnie dokładnie 20 bajtów.")
        print("Odebrano tekst:", surowe_dane.decode())
    except ConnectionError as e:
        print("Błąd sieciowy:", e)