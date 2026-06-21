import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 2912))
s.listen(1)
print("Testowy serwer gry uruchomiony na porcie 2912...")

try:
    while True:
        conn, addr = s.accept()
        print(f"Połączono z {addr}")
        tajna_liczba = random.randint(1, 100)
        print(f"Wylosowana liczba dla tego połączenia: {tajna_liczba}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Klient {addr} rozłączył się.")
                    break

                try:
                    wiadomosc = data.decode('utf-8').strip()
                    if not wiadomosc:
                        continue

                    strzal = int(wiadomosc)
                    print(f"Klient strzela: {strzal}")

                    if strzal == tajna_liczba:
                        conn.sendall(b"Zgadles!\n")
                        break
                    elif strzal < tajna_liczba:
                        conn.sendall(b"Za malo\n")
                    else:
                        conn.sendall(b"Za duzo\n")

                except ValueError:
                    conn.sendall(b"Blad: Podaj poprawna liczbe!\n")
except KeyboardInterrupt:
    print("\nSerwer zatrzymany.")
finally:
    s.close()