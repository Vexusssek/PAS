import socket

HOST = '127.0.0.1'
PORT = 2907

print("dns udp")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serwer nasłuchuje na porcie {PORT}...")

    while True:
        try:
            data, addr = s.recvfrom(1024)
            hostname_do_sprawdzenia = data.decode().strip()
            print(
                f"Otrzymano zapytanie od {addr} o hostname: {hostname_do_sprawdzenia}"
            )

            try:
                ip_address = socket.gethostbyname(hostname_do_sprawdzenia)
                odpowiedz = ip_address
            except socket.gaierror:
                odpowiedz = (
                    "Blad: Nie mozna znalezc adresu IP dla podanego hostname."
                )
            except Exception as e:
                odpowiedz = f"Blad serwera: {e}"

            s.sendto(odpowiedz.encode(), addr)
            print(f"Wysłano odpowiedź: {odpowiedz}")
            print("-" * 40)

        except KeyboardInterrupt:
            print("\nZamykanie serwera.")
            break