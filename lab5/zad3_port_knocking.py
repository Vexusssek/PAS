import socket, time

def port_knocking(host='127.0.0.1'): #port tutaj podmieniłem na serwer lokalny (z pliku zad3_serwer_testowy)
    znalezione = []
    print("1. Skanowanie...")
    for i in range(65):
        port = i * 1000 + 666
        if port > 65535: break

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(0.2)
            try:
                s.sendto(b"PING", (host, port))
                if b"PONG" in s.recv(1024):
                    print(f" -> Wykryto port UDP: {port}")
                    znalezione.append(port)
            except:
                pass

    if not znalezione: return print("Brak portów.")

    print(f"2. Port Knocking (PING-PONG) do: {znalezione}")
    for port in znalezione:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1.0)
            try:
                s.sendto(b"PING", (host, port))
                s.recv(1024)
            except:
                pass
            time.sleep(0.1)

    print("3. Połączenie TCP...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((host, 2913))
            print(f"Wynik: {s.recv(1024).decode('utf-8').strip()}")
    except Exception as e:
        print(f"Błąd TCP: {e}")


if __name__ == "__main__":
    port_knocking('127.0.0.1')