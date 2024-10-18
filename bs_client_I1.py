import socket
import sys

host = '10.1.1.2'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
try:
          

         with s.connect((host, port)) :

              s.sendall(b'Meoooo !')

              data = s.recv(1024)
              if data:
               print(f"Le serveur a répondu {repr(data)}")
         sys.exit(0)

except Exception as e:
   print(f"Error : {e}")

   sys.exit(1)

