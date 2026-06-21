import socket
import time

def measure_tcp(host, port, iterations=100):
    msg = b"PING"
    times = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for _ in range(iterations):
            start = time.perf_counter()
            s.sendall(msg)
            data = s.recv(1024)
            end = time.perf_counter()
            times.append(end - start)
            
    avg = sum(times) / iterations
    return avg

def measure_udp(host, port, iterations=100):
    msg = b"PING"
    times = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for _ in range(iterations):
            start = time.perf_counter()
            s.sendto(msg, (host, port))
            data, addr = s.recvfrom(1024)
            end = time.perf_counter()
            times.append(end - start)
            
    avg = sum(times) / iterations
    return avg

if __name__ == "__main__":
    HOST = '127.0.0.1'
    TCP_PORT = 12345
    UDP_PORT = 12346
    N = 1000
    
    print(f"Wykonuje {N} prob dla kazdego protokolu...")
    
    tcp_avg = measure_tcp(HOST, TCP_PORT, N)
    print(f"Sredni czas TCP: {tcp_avg:.8f} s")
    
    udp_avg = measure_udp(HOST, UDP_PORT, N)
    print(f"Sredni czas UDP: {udp_avg:.8f} s")
    
"""
Odpowiedzi na pytania z zadania:
1. Dla którego z gniazd czas jest krótszy?
   - Krótszy czas uzyskałem dla gniazda UDP.

2. Z czego wynika krótszy czas?
   - Wynika to z braku mechanizmów kontroli przepływu, nawiązywania połączenia (tzw. brak 3-way handshake),
     potwierdzeń odbioru (ACK) oraz mniejszego narzutu nagłówków w protokole UDP.

3. Jakie są zalety / wady obu rozwiązań?
   - TCP: 
     * Zalety: niezawodność, gwarancja dostarczenia pakietów i zachowania ich kolejności.
     * Wady: wolniejszy protokół, większy narzut sieciowy i nagłówkowy.
   - UDP: 
     * Zalety: maksymalna szybkość, minimalny narzut transmisyjny.
     * Wady: brak gwarancji dostarczenia pakietów oraz brak kontroli ich kolejności.
"""
