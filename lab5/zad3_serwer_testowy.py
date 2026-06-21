import socket
import threading
import time

HOST = '127.0.0.1'
TCP_PORT = 2913
UKRYTE_PORTY_UDP = [5666, 15666]

historia_pukania = {}
odblokowane_ip = set()


def obsluga_udp(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, port))
        while True:
            data, addr = s.recvfrom(1024)
            if data.decode('utf-8').strip() == "PING":
                s.sendto(b"PONG", addr)

                client_ip = addr[0]
                if client_ip not in historia_pukania:
                    historia_pukania[client_ip] = []

                if port not in historia_pukania[client_ip]:
                    historia_pukania[client_ip].append(port)

                if historia_pukania[client_ip] == UKRYTE_PORTY_UDP:
                    print(f"[SERWER] Sukces! {client_ip} odblokował port TCP.")
                    odblokowane_ip.add(client_ip)
                    historia_pukania[client_ip] = []


def start_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, TCP_PORT))
        s.listen(5)
        print(f"[SERWER] Usługa TCP, na porcie {TCP_PORT}...")

        while True:
            conn, addr = s.accept()
            client_ip = addr[0]
            with conn:
                if client_ip in odblokowane_ip:
                    conn.sendall(b"Congratulations! You found the hidden.\n")
                    odblokowane_ip.remove(client_ip)
                else:
                    print(f"[SERWER] Blokada zapory sieciowej dla {addr}")
                    conn.close()


if __name__ == "__main__":
    print("Uruchamianie serwera testowego Port-Knocking...")
    for port in UKRYTE_PORTY_UDP:
        threading.Thread(target=obsluga_udp, args=(port,), daemon=True).start()
        print(f"[SERWER] Otwarto port UDP: {port}")

    try:
        start_tcp()
    except KeyboardInterrupt:
        print("\nSerwer wyłączony.")