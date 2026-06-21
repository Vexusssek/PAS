import socket
import sys

def start_client(host='127.0.01', port=2912): #zmieniłem adres na lokalny testowego serwera
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            print(f"Próba połączenia z serwerem {host}:{port}...")
            s.connect((host, port))
            print("Połączono pomyślnie!")

            while True:
                guess = input("Podaj liczbę (lub 'q' aby wyjść): ").strip()
                if guess.lower() == 'q':
                    print("Zamykanie połączenia.")
                    break

                if not guess.isdigit():
                    print("To nie jest prawidłowa liczba naturalna!")
                    continue

                s.sendall(guess.encode('utf-8'))

                data = s.recv(1024)
                if not data:
                    print("Serwer zamknął połączenie.")
                    break

                response = data.decode('utf-8', errors='replace').strip()
                print(f"Odpowiedź serwera: {response}")

                if "zgad" in response.lower():
                    print("Gratulacje! Koniec rozgrywki.")
                    break

    except socket.timeout:
        print("Błąd: Przekroczono czas oczekiwania na odpowiedź serwera (timeout).")
    except Exception as e:
        print(f"Błąd połączenia: {e}")
    except KeyboardInterrupt:
        print("\nKlient zatrzymany przez użytkownika.")

if __name__ == "__main__":
    target_host = '127.0.0.1'
    target_port = 2912

    start_client(target_host, target_port)