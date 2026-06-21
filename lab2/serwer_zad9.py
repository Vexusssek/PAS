import socket

HOST = '127.0.0.1'
PORT = 2906

print("dns udp")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serwer nasłuchuje na porcie {PORT}...")

    while True:
        try:
            data, addr = s.recvfrom(1024)
            ip_do_sprawdzenia = data.decode().strip()
            print(f"Otrzymano zapytanie od {addr} o adres IP: {ip_do_sprawdzenia}")

            try:
                hostname = socket.gethostbyaddr(ip_do_sprawdzenia)[0]
                odpowiedz = hostname
            except socket.herror:
                odpowiedz = "Blad: Nie znaleziono nazwy hosta dla tego IP (brak rekordu PTR)."
            except Exception as e:
                odpowiedz = f"Blad serwera: {e}"

            s.sendto(odpowiedz.encode(), addr)
            print(f"Wysłano odpowiedź: {odpowiedz}")
            print("-" * 40)

        except KeyboardInterrupt:
            print("\nZamykanie serwera DNS.")
            break