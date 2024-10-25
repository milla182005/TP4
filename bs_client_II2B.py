import logging
import socket


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('/home/ingrid/logs/bs_client.log')  
    ]
)

def connect_to_server(ip, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((ip, port))
            logging.info(f"Connexion réussie à {ip}:{port}.")
            
           
            client_socket.sendall(message.encode())
            logging.info(f"Message envoyé au serveur {ip}:{port} : \"{message}\".")
            
            
            response = client_socket.recv(1024).decode()
            logging.info(f"Réponse reçue du serveur {ip}:{port} : \"{response}\".")
    except ConnectionRefusedError:
        logging.error(f"Impossible de se connecter au serveur {ip} sur le port {port}.")
    except socket.error as e:
        logging.error(f"Erreur de connexion : {e}")

if __name__ == "__main__":
    connect_to_server('127.0.0.1', 8888, "Hello, Server!")  
