import socket

HOST = '127.0.0.1'
PORT = 2901

print("serwer udp")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serwer UDP nasłuchuje na porcie {PORT}...")

    data, addr = s.recvfrom(1024)
    print(f"Otrzymano wiadomość od {addr}: {data.decode()}")

    odpowiedz = b"Wiadomosc UDP odebrana pomyslnie!"
    s.sendto(odpowiedz, addr)
    print("Odpowiedź wysłana. Zamykam serwer.")