import logging
import socket
import re

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('/home/ingrid/logs/bs_client.log')
    ]
)


def validate_expression(expression):
    pattern = r"^(-?\d{1,6})\s*([\+\-\*])\s*(-?\d{1,6})$"
    return re.match(pattern, expression)

def connect_to_server(ip, port):
    while True:
        operation = input("Entrez une opération (ex: 3 + 4, -5 * 2) : ")
        
     
        if not validate_expression(operation):
            print("Opération invalide. Réessayez.")
            continue

        try:
           
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((ip, port))
                logging.info(f"Connexion réussie à {ip}:{port}.")

            
                client_socket.sendall(operation.encode())
                logging.info(f"Opération envoyée au serveur {ip}:{port} : \"{operation}\".")

              
                response = client_socket.recv(1024).decode()
                logging.info(f"Réponse reçue du serveur {ip}:{port} : \"{response}\".")
                print(f"Résultat : {response}")

        except ConnectionRefusedError:
            logging.error(f"Impossible de se connecter au serveur {ip} sur le port {port}.")
            break

if __name__ == "__main__":
    connect_to_server('10.1.1.2', 8888)



