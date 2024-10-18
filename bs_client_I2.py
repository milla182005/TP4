import socket
import sys

host = '10.1.1.2'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
try:
    data = s.recv(1024)
    
    print(f"{data.decode()}")

    user_input = input("Que veux-tu envoyer au serveur : ")
    s.sendall(user_input.encode())

    data = s.recv(1024)
    if data:
        print(f"Réponse du serveur : {repr(data)}")

        sys.exit(0)

except Exception as e:
   print(f"Error :Impossible de se connecter au serveur {host} sur le port {port}. Détails {e}")

   sys.exit(1)

