# Fase 3 - Herencia y Polimorfismo

## Objetivo

En esta fase vamos a modelar los distintos tipos de animales de la tienda utilizando los principios más importantes de la Programación Orientada a Objetos.

Aprenderás:

- Herencia
- Clases abstractas
- Polimorfismo
- Sobrescritura de métodos
- Uso de colecciones polimórficas

---

# Escenario

Hasta ahora todas las mascotas eran objetos de tipo `Mascota`.

Sin embargo, cada animal tiene comportamientos diferentes:

```text
Perro -> Ladra
Gato -> Maúlla
Ave -> Pía
Pez -> No emite sonido
```

Vamos a representar estas diferencias usando herencia.

---

# Paso 1. Crear la clase abstracta Animal

Archivo:

```text
lib/models/animal.dart
```

```dart
abstract class Animal {
  final String nombre;
  final int edad;

  Animal(this.nombre, this.edad);

  void emitirSonido();

  void mostrarFicha() {
    print('$nombre - $edad años');
  }
}
```

---

# Paso 2. Crear la clase Perro

Archivo:

```text
lib/models/perro.dart
```

```dart
import 'animal.dart';

class Perro extends Animal {
  Perro(String nombre, int edad)
      : super(nombre, edad);

  @override
  void emitirSonido() {
    print('Guau');
  }
}
```

---

# Paso 3. Crear la clase Gato

```dart
import 'animal.dart';

class Gato extends Animal {
  Gato(String nombre, int edad)
      : super(nombre, edad);

  @override
  void emitirSonido() {
    print('Miau');
  }
}
```

---

# Paso 4. Crear la clase Ave

```dart
import 'animal.dart';

class Ave extends Animal {
  Ave(String nombre, int edad)
      : super(nombre, edad);

  @override
  void emitirSonido() {
    print('Pío');
  }
}
```

---

# Paso 5. Crear la clase Pez

```dart
import 'animal.dart';

class Pez extends Animal {
  Pez(String nombre, int edad)
      : super(nombre, edad);

  @override
  void emitirSonido() {
    print('...');
  }
}
```

---

# Paso 6. Utilizar las clases

```dart
void main() {
  final perro = Perro('Toby', 2);

  perro.mostrarFicha();
  perro.emitirSonido();
}
```

Salida:

```text
Toby - 2 años
Guau
```

---

# Paso 7. Polimorfismo

Ahora todas las clases heredan de `Animal`.

Podemos almacenarlas en la misma colección.

```dart
List<Animal> animales = [
  Perro('Toby', 2),
  Gato('Luna', 1),
  Ave('Piolín', 1),
  Pez('Nemo', 1),
];
```

---

# Paso 8. Ejecutar comportamientos polimórficos

```dart
for (final animal in animales) {
  animal.emitirSonido();
}
```

Resultado:

```text
Guau
Miau
Pío
...
```

Aunque todos son tratados como `Animal`, cada uno ejecuta su propia implementación.

---

# Paso 9. Sobrescribir mostrarFicha()

Ejemplo para Perro:

```dart
@override
void mostrarFicha() {
  print(
    'PERRO: $nombre - $edad años'
  );
}
```

---

# Paso 10. Añadir nuevas propiedades

```dart
class Perro extends Animal {
  final String raza;

  Perro(
    String nombre,
    int edad,
    this.raza,
  ) : super(nombre, edad);

  @override
  void emitirSonido() {
    print('Guau');
  }
}
```

Uso:

```dart
final perro = Perro(
  'Toby',
  2,
  'Labrador',
);
```

---

# Paso 11. Integración con la tienda

Crear inventario:

```dart
List<Animal> inventario = [
  Perro('Toby', 2, 'Labrador'),
  Gato('Luna', 1),
  Ave('Piolín', 1),
  Pez('Nemo', 1),
];
```

Mostrar catálogo:

```dart
for (final animal in inventario) {
  animal.mostrarFicha();
}
```

---

# Paso 12. Comprobar tipos

```dart
if (animal is Perro) {
  print('Es un perro');
}
```

```dart
if (animal is Gato) {
  print('Es un gato');
}
```

---

# Ejercicio práctico

Crear una nueva clase:

```text
Conejo
```

Que herede de:

```dart
Animal
```

Y que implemente:

```dart
emitirSonido()
```

Mostrando:

```text
Sniff
```

---

# Mini proyecto

Crear una lista con:

```text
Toby (Perro)
Luna (Gato)
Piolín (Ave)
Nemo (Pez)
Bugs (Conejo)
```

Recorrer la colección mostrando:

```text
Nombre
Edad
Sonido
```

---

# Conceptos aprendidos

| Concepto | Ejemplo |
|-----------|----------|
| Herencia | Perro extiende Animal |
| Clase abstracta | Animal |
| Método abstracto | emitirSonido() |
| Override | Personalizar comportamiento |
| Polimorfismo | List<Animal> |
| Especialización | Perro, Gato, Ave, Pez |
| Operador is | Comprobación de tipos |

---

# Reto final

Implementa un método:

```dart
void presentar()
```

Que muestre algo como:

```text
Hola, soy Toby.
Soy un perro.
Tengo 2 años.
Guau.
```

Cada animal deberá tener una presentación distinta aprovechando el polimorfismo.


