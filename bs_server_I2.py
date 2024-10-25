import socket

host = '10.1.1.2'
port = 13337

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

conn.close()

