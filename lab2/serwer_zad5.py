import socket

HOST = '127.0.0.1'
PORT = 2902

print("serwer udp")
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serwer nasłuchuje w pętli na porcie {PORT}...")

    while True:
        try:
            data, addr = s.recvfrom(1024)
            wiadomosc = data.decode('utf-8', errors='ignore')

            print(f"[{addr[0]}:{addr[1]}] Przesłał: {wiadomosc}")

            odpowiedz = f"Serwer odebrał: {wiadomosc}"

            s.sendto(odpowiedz.encode('utf-8'), addr)

        except KeyboardInterrupt:
            print("\nZamykanie serwera.")
            break