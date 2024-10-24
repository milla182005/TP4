import argparse
import socket
import sys

def check_port(port):
    try:
        port = int(port)
    except ValueError:
        print(f"ERROR -p argument invalide. Le port spécifié {port} n'est pas un entier.")
        sys.exit(1)

    if port < 0 or port > 65535:
        print(f"ERROR -p argument invalide. Le port spécifié {port} n'est pas un port valide (de 0 à 65535).")
        raise SystemExit(1)
    elif port >= 0 and port <= 1024:
        print(f"ERROR -p argument invalide. Le port spécifié {port} est un port privilégié. Spécifiez un port au dessus de 1024.")
        raise SystemExit(2)

    return port

def check_ip(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        print(f"ERROR -l argument invalide. L'adresse {ip} n'est pas une adresse IP valide.")
        sys.exit(3)

    local_ips = socket.gethostbyname_ex(socket.gethostname())[2]
    if ip not in local_ips:
        print(f"ERROR -l argument invalide. L'adresse {ip} n'est pas l'une des adresses IP de cette machine.")
        raise SystemExit(4)

    return ip

parser = argparse.ArgumentParser(
    description="Lance un serveur qui écoute sur une IP et un port spécifiques.",
    usage="python bs_server_II1.py [-p PORT] [-l IP]",
)

parser.add_argument("-p", "--port", type=check_port, default=13337, help="Le port sur lequel le serveur écoute (par défaut 13337)")

parser.add_argument("-l", "--listen", type=check_ip, required=True, help="L'adresse IP sur laquelle le serveur écoute")

args = parser.parse_args()

print(f"Le serveur va écouter sur l'adresse {args.listen} et le port {args.port}.")



