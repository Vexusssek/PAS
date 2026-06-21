import socket

def start_server(host='127.0.0.1', port=12346):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f"Zadanie 2: Serwer TCP Echo działający na {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Połączono z {addr}")
                data = conn.recv(1024)
                if data:
                    conn.sendall(data)
                    print(f"Odesłano: {data.decode('utf-8', errors='replace')}")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
