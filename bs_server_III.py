import logging
import socket

# Configuration des logs
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('/var/log/bs_server/bs_server.log')
    ]
)

def start_server(ip, port):
    # Création et configuration du socket serveur
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((ip, port))
        server_socket.listen()
        logging.info(f"Serveur lancé sur {ip}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            logging.info(f"Un client ({client_address[0]}) s'est connecté.")

            with client_socket:
                # Recevoir l'opération du client
                operation = client_socket.recv(1024).decode()
                logging.info(f"Opération reçue du client {client_address[0]} : \"{operation}\"")

                try:
                    # Calculer le résultat de l'opération
                    result = eval(operation)
                    logging.info(f"Résultat de l'opération : {result}")
                    client_socket.sendall(str(result).encode())

                except Exception as e:
                    # En cas d'erreur de calcul, renvoyer un message d'erreur au client
                    error_msg = "Erreur dans l'opération."
                    logging.error(f"Erreur de calcul pour l'opération '{operation}': {e}")
                    client_socket.sendall(error_msg.encode())

if __name__ == "__main__":
    start_server('127.0.0.1', 8888)