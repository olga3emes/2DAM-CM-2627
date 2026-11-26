#Validar contraseña fuerte
#
# Debe contener:
#
# Al menos 8 caracteres
# Una mayúscula
# Una minúscula
# Un número


password=input("Password: ")
mayuscula= False
minuscula = False
numero = False

for c in password:
    if c.isupper():
        mayuscula = True
    elif c.islower():
        minuscula = True
    elif c.isdigit():
        numero = True

if(mayuscula and minuscula and numero and len(password)>=8):
    print("La password es válida")
else:
    print("La contraseña no cumple los requisitos")