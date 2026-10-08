import hashlib
# Ejemplo de uso de hashlib para crear hashes de un texto
texto = "hola mundo".encode()
# Hash MD5
md5 = hashlib.md5(texto).hexdigest()
print("MD5:", md5)
# Hash SHA-1
sha1 = hashlib.sha1(texto).hexdigest()
print("SHA-1:", sha1)
# Hash SHA-256
sha256 = hashlib.sha256(texto).hexdigest()
print("SHA-256:", sha256)
# Hash SHA-512
sha512 = hashlib.sha512(texto).hexdigest()
print("SHA-512:", sha512)

import hmac
import hashlib
# Ejemplo de uso de HMAC con SHA-256
mensaje = b"mensaje secreto"
clave = b"clave_compartida"
firma = hmac.new(clave, mensaje, hashlib.sha256).hexdigest()
print("HMAC (SHA-256):", firma)

import secrets
import string
# Token hexadecimal aleatorio
print("Token seguro:", secrets.token_hex(16))
# Contraseña segura de 12 caracteres
alfabeto = string.ascii_letters + string.digits
contrasenya = ''.join(secrets.choice(alfabeto) for _ in range(12))
print("Contraseña segura:", contrasenya)

