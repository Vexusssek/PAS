import socket
import random
import sys

def start_server(host='127.0.0.1', port=2912):
    target_number = random.randint(1, 100)
    print(f"Zadanie 2: Serwer TCP Guessing Game na {host}:{port}")
    print(f"[DEBUG] Wylosowana liczba: {target_number}")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Polaczono z {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                
                msg = data.decode('utf-8').strip()
                print(f"Odebrano: {msg}")
                
                try:
                    guess = int(msg)
                    if guess < target_number:
                        response = "Twoja liczba jest mniejsza od wylosowanej."
                    elif guess > target_number:
                        response = "Twoja liczba jest wieksza od wylosowanej."
                    else:
                        response = "Gratulacje! Odgadles liczbe."
                        conn.sendall(response.encode('utf-8'))
                        print("Liczba odgadnieta. Serwer konczy dzialanie.")
                        return
                        
                    conn.sendall(response.encode('utf-8'))
                except ValueError:
                    response = "Blad: Przeslana wiadomosc nie jest liczba."
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    port = 2912
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
        
    try:
        start_server(port=port)
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
