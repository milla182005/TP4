import socket
import sys
import argparse
from datetime import datetime


def check_port(port):
    port = int(port)
    if port < 1024 or port > 65535:
        print("Le port doit être entre 1024 et 65535.")
    return port

def check_ip(ip):
    return ip

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", type=check_port, default=13337, help="Le port sur lequel le serveur écoute (par défaut 13337)")

parser.add_argument("-l", "--listen", type=check_ip, required=True, help="L'adresse IP sur laquelle le serveur écoute")

args = parser.parse_args()

host = args.listen
port = args.port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
try:
    data = s.recv(1024)

    print(f"{data.decode()}")

    user_input = input("Que veux-tu envoyer au serveur : ")
    s.sendall(user_input.encode())

    data = s.recv(1024)
    if data:
        print(f"Réponse du serveur : {data.decode()}")

        sys.exit(0)

except Exception as e:
   print(f"Error :Impossible de se connecter au serveur {host} sur le port {port}. Détails {e}")

   sys.exit(1)

   def log(msg: str, log_level: str):
           now = datetime.now()
           with open('/tmp/bs_client_II2B.log', "a") as log_file:
             log_file.write(f"{now} {log_level} {msg}\n")
log("INFO", "Connexion réussie à <IP>:<PORT>.")


