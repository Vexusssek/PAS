import socket

HOST = '127.0.0.1'
PORT = 2903

print("serwer udp zad 6")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serwer czeka na obliczenia na porcie {PORT}...")

    while True:
        try:
            data, addr = s.recvfrom(1024)
            rownanie = data.decode().strip()
            print(f"Otrzymano zadanie od {addr}: {rownanie}")

            elementy = rownanie.split()

            if len(elementy) != 3:
                wynik = "Blad: Niepoprawny format wiadomosci."
            else:
                l1_str, op, l2_str = elementy
                try:
                    l1 = float(l1_str)
                    l2 = float(l2_str)

                    if op == '+':
                        wynik = str(l1 + l2)
                    elif op == '-':
                        wynik = str(l1 - l2)
                    elif op == '*':
                        wynik = str(l1 * l2)
                    elif op == '/':
                        if l2 == 0:
                            wynik = "Blad: Dzielenie przez zero!"
                        else:
                            wynik = str(l1 / l2)
                    else:
                        wynik = f"Blad: Nieznany operator '{op}'"
                except ValueError:
                    wynik = "Blad: Podane argumenty nie sa liczbami."

            s.sendto(wynik.encode(), addr)
            print(f"Wysłano odpowiedź: {wynik}")
            print("-" * 40)

        except KeyboardInterrupt:
            print("\nZamykanie serwera kalkulatora.")
            break