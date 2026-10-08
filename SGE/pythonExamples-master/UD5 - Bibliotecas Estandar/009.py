import socket
# Cliente TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("example.com", 80))
# Enviar una solicitud HTTP simple
cliente.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
respuesta = cliente.recv(4096)
print(respuesta.decode())
cliente.close()


import http.client
conn = http.client.HTTPSConnection("www.example.com")
conn.request("GET", "/")
respuesta = conn.getresponse()
print("Status:", respuesta.status)
print("Contenido:", respuesta.read().decode())
conn.close()

import urllib.request
import urllib.parse

url = "https://httpbin.org/get"
respuesta = urllib.request.urlopen(url)
print("Código HTTP:", respuesta.getcode())
print("Contenido:", respuesta.read().decode())


# Ejecuta este script en terminal
from http.server import SimpleHTTPRequestHandler, HTTPServer
puerto = 8000
servidor = HTTPServer(("localhost", puerto), SimpleHTTPRequestHandler)
print(f"Servidor en http://localhost:{puerto}")
servidor.serve_forever()

import smtplib

# ATENCIÓN: para funcionar necesitamos una cuenta SMTP válida
remitente = "tucorreo@example.com"
destinatario = "destino@example.com"
mensaje = "Subject: Prueba SMTP\n\nEste es un mensaje enviado desde Python."

with smtplib.SMTP("smtp.example.com", 587) as servidor:
    servidor.starttls()
    servidor.login("usuario", "contraseña")
    servidor.sendmail(remitente, destinatario, mensaje)

import imaplib
# ATENCIÓN: solo si tienes servidor IMAP real
mail = imaplib.IMAP4_SSL("imap.example.com")
mail.login("usuario", "contraseña")
mail.select("inbox")
status, mensajes = mail.search(None, "ALL")
print("IDs de mensajes:", mensajes)
mail.logout()

from ftplib import FTP
# FTP público de prueba (anónimo)
ftp = FTP("ftp.debian.org")
ftp.login()
ftp.cwd("debian")
ftp.retrlines("LIST")
ftp.quit()
