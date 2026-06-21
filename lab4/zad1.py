import socket
import datetime

def start_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f"Zadanie 1: Serwer TCP działający na {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Połączono z {addr}")
                data = conn.recv(1024)
                if data:
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    conn.sendall(now.encode('utf-8'))
                    print(f"Wysłano: {now}")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
