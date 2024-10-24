import logging
import socket
import time
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(),  
        logging.FileHandler('/var/log/bs_server/bs_server.log')  
    ]
)

def start_server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((ip, port))
        server_socket.listen()

        logging.info("Lancement du serveur")
        logging.info(f"Le serveur tourne sur {ip}:{port}")

        last_client_time = datetime.now()

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                with client_socket:
                    logging.info(f"Un client ({client_address[0]}) s'est connecté.")
                    last_client_time = datetime.now()

                    message = client_socket.recv(1024).decode()
                    if message:
                        logging.info(f"Le client {client_address[0]} a envoyé \"{message}\".")
                        response = f"Message reçu : {message}"
                        client_socket.sendall(response.encode())
                        logging.info(f"Réponse envoyée au client {client_address[0]} : \"{response}\".")
            except Exception as e:
                logging.error(f"Erreur lors de la connexion avec le client : {e}")

            if (datetime.now() - last_client_time).seconds > 60:
                logging.warning("Aucun client connecté depuis plus d'une minute.")
                time.sleep(60)  
if __name__ == "__main__":
    start_server('10.1.1.2', 8888)  

