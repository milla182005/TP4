import socket
import argparse
from datetime import datetime
from sys import exit as sysexit

def check_port(port):
    if port < 1024 or port > 65535:
        print("erreur")
        sysexit(1)
    return port

def check_ip(ip):
    return ip


parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", type=check_port, default=13337, help="Le port sur lequel le serveur écoute (par défaut 13337)")

parser.add_argument("-l", "--listen", type=check_ip, required=True, help="L'adresse IP sur laquelle le serveur écoute")

args = parser.parse_args()

host = args.listen
port = args.port

print(f"Le serveur va écouter sur l'adresse {args.listen} et le port {args.port}.")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


print(f"Serveur en écoute sur {host}:{port}")


while True:
        s.listen(1)
        conn, addr = s.accept()

        print(f"Un client vient de se co et son IP c'est {addr[0]}.")
        
        conn.sendall(b"Hi mate !")

        try:
            data = conn.recv(1024)
            if not data: break
            client_message = data.decode()
            print(f"Message reçu du client: {client_message}")

            if "meo" in client_message.lower():
                        response = "Meo à toi confrère."
            elif "waf" in client_message.lower():
                        response = "ptdr t ki"
            else:
                        response = "Mes respects humble humain."

            conn.sendall(response.encode())

        except socket.error:
          print("Erreur lors de la réception du message.")

          def log(msg: str, log_level: str):
           now = datetime.now()
           with open('/tmp/bs_client_II2B.log', "a") as log_file:
             log_file.write(f"{now} {log_level} {msg}\n")
log("INFO", "Le serveur tourne sur <IP>:<port>")


conn.close()

