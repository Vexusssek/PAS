import socket

def recv_exactly(conn, n):
    buf = b''
    while len(buf) < n:
        chunk = conn.recv(n - len(buf))
        if not chunk:
            return None
        buf += chunk
    return buf

def send_exactly(conn, data):
    total_sent = 0
    while total_sent < len(data):
        sent = conn.send(data[total_sent:])
        if sent == 0:
            raise RuntimeError("Polaczenie przerwane")
        total_sent += sent

def start_server(host='127.0.0.1', port=12352):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f"Zadanie 8: Serwer TCP (pewnosc 20 znakow) na {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                data = recv_exactly(conn, 20)
                if data:
                    msg = data.decode('utf-8', errors='replace')
                    send_exactly(conn, data)
                    print(f"Odebrano i wyslano dokladnie 20 bajtow: '{msg}'")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
