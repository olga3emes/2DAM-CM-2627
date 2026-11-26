from Ejercicios.Videojuego import Videojuego

v1 = Videojuego(1,"La vida de Rafal", 30000)
v2 = Videojuego(2, "GTA VI", 60)
v3 = Videojuego(3, "The Legend of Zelda: Ocarina of Time", 100)


videojuegos={v1,v2,v3}

for videojuego in videojuegos:
    print(videojuego)

v4 = v1.__copy__();
v5 = v2.__deepcopy__(v2);

print(v4);
print(v5);

print(v4.__hash__());
print(v1.__hash__());
v1.titulo = "La vida de Rafal 2";
print(v1.titulo);
print(v4.titulo);
v2.titulo = "GTA VII";
print(v5.titulo);
print(v2.titulo);
