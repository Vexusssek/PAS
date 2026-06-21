import socket
import threading

def tcp_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        print(f"TCP Serwer nasluchuje na {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

def udp_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP Serwer nasluchuje na {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            s.sendto(data, addr)

if __name__ == "__main__":
    HOST = '127.0.0.1'
    TCP_PORT = 12345
    UDP_PORT = 12346
    
    t1 = threading.Thread(target=tcp_server, args=(HOST, TCP_PORT), daemon=True)
    t2 = threading.Thread(target=udp_server, args=(HOST, UDP_PORT), daemon=True)
    
    t1.start()
    t2.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Serwery zatrzymane.")
