import socket
import time

def invia_syn_ack(destinazione, porta, quantita_syn_ack, velocita_syn_ack):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.settimeout(2)
        sock.connect((destinazione, porta))
        for i in range(quantita_syn_ack):
            if (i + 1) % 50 == 0:  
                print("\033[1;34mSYN/ACK inviato con successo\033[0m")
            else:
                print("\033[1;32mSYN/ACK packet inviato con successo\033[0m")
            time.sleep(velocita_syn_ack)
    except Exception as e:
        print("\033[1;31mSYN/ACK invio fallito: {}\033[0m".format(e))
    finally:
        sock.close()

print("\033[1;32m⣿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿⣿⠟⣿⣿⢿⣿⢿⣿⢿⣿⢿⣿⢿\033[0m")
print("\033[1;32m⣿⣯⣿⢯⣿⣯⣿⢯⣿⣯⣿⠫⡿⣯⣿⣯⣟⠁⠀⢿⣿⣻⣯⣿⢯⣿⣯⣿⢯⣿\033[0m")
print("\033[1;32m⣿⣟⣾⡿⣟⣾⣿⣻⣿⠾⠃⢀⠀⡀⠿⠯⠏⠀⠌⣼⣿⢿⣽⣾⡿⣟⣾⣿⣻⣿\033[0m")
print("\033[1;32m⣿⡿⣽⣿⡛⠛⠚⣿⣟⣷⠄⠂⢰⣤⠀⠄⠠⢈⠠⢹⣿⢿⣻⣾⢿⣟⣿⡾⣿⣽\033[0m")
print("\033[1;32m⣿⣿⣻⣷⣿⣄⡂⠈⠉⡀⠠⢈⠘⠟⠀⠠⠁⡄⠂⡁⡸⠻⣿⣽⡿⣯⣿⣽⡿⣽\033[0m")
print("\033[1;32m⣿⣷⢿⣳⣿⢿⣷⣧⠐⠀⡁⢀⠂⠈⡄⠑⠡⢀⠂⡐⠀⠀⠈⠳⣿⢿⣽⣾⢿⣿\033[0m")
print("\033[1;32m⣿⣯⣿⢿⣽⡿⣯⡿⠀⠒⠰⠀⡈⠌⠐⢈⠠⠀⠄⠀⠀⠀⠀⠀⣿⣿⣻⣾⢿⣻\033[0m")
print("\033[1;32m⣿⣟⣾⡿⣯⣿⣟⣇⠠⠈⡴⡇⠀⡐⠈⡀⠀⠉⣤⣶⣤⠀⠀⠀⣾⣿⣽⢿⣻⣿\033[0m")
print("\033[1;32m⣿⡿⣽⣿⣻⣷⠟⠛⠀⠄⢟⡇⠠⣸⠀⣠⠀⢸⣿⣭⣿⡗⠀⠸⢿⣳⣿⢿⣻⣽\033[0m")
print("\033[1;32m⣿⣿⣻⣷⢿⣻⣦⣤⢈⡄⠀⡁⠐⣀⠵⠟⠧⠀⠙⠛⠉⠀⢀⣀⣼⡿⣯⣿⣟⣿\033[0m")
print("\033[1;32m⣿⣷⢿⣯⣿⣟⣿⢿⡿⣇⠐⣦⡅⠀⢠⠀⠀⡀⢠⣶⠇⢰⣿⡿⣯⣿⣟⣷⣿⣻\033[0m")
print("\033[1;32m⣿⣯⣿⣟⣾⡿⣽⣿⣻⣿⡀⢻⣿⣤⣇⣼⣔⣷⣾⡟⠀⣿⡿⣽⣿⣳⣿⣻⣾⢿\033[0m")
print("\033[1;32m⣿⣟⣾⡿⣽⣿⣻⣷⢿⣻⡃⢈⡋⠿⠹⠛⡟⢻⠉⠁⠀⣿⢿⣟⣷⡿⣯⣿⣽⣿\033[0m")
print("\033[1;32m⣿⡿⣽⣿⣻⣷⢿⣯⣿⢿⣷⣤⡈⠉⠂⠋⠓⠩⢁⣴⣾⢿⣟⣯⣿⣟⣿⡷⣿⣾\033[0m")
print("\033[1;32m⣿⣿⣻⣷⢿⣯⣿⣟⣾⡿⣯⣿⢿⣦⣥⣦⣴⣷⡿⣿⣽⣿⣻⣯⣷⡿⣯⣿⢿⣽\033[0m")


if __name__ == "__main__":
    print("\033[1;31mDEVASTER DDoS SYN/ACK BRUTE\nby t.me/VikingTERMINAL\033[0m")
    destinazione = input("\033[1;35mInserisci l'indirizzo IP o il dominio per effettuare il test: \033[0m")
    porta = int(input("\033[1;35mInserisci il numero di porta: \033[0m"))
    quantita_syn_ack = int(input("\033[1;35mInserisci la quantità di pacchetti: \033[0m"))
    velocita_syn_ack = float(input("\033[1;35mInserisci la velocità di invio (in millisecondi): \033[0m"))
    invia_syn_ack(destinazione, porta, quantita_syn_ack, velocita_syn_ack)
