import socket

HOST = '127.0.0.1'
PORT = 2900

print("Uruchamiam serwer testowy TCP...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serwer nasłuchuje na porcie {PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"Połączono z klientem o adresie: {addr}")
        data = conn.recv(1024)
        if data:
            print(f"Serwer otrzymał: {data.decode()}")
            conn.sendall(b"Wiadomosc odebrana!")