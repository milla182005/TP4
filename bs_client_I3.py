import socket
import sys
import re

HOST = '10.1.1.2'
PORT = 13337

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connecté avec succès au serveur {HOST} sur le port {PORT}")

        message = input("Que veux-tu envoyer au serveur : ")

        if not isinstance(message, str):
            raise TypeError("Le message doit être une chaîne de caractères.")
        
        if not re.search(r'(meo|waf)', message.lower()):
            raise ValueError("Le message doit contenir soit 'meo' soit 'waf'.")

        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Réponse du serveur: {data.decode()}")

except (TypeError, ValueError) as e:
    print(f"Erreur: {e}")
finally:
    sys.exit(0)
