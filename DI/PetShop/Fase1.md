# Fase 1 - Programación Orientada a Objetos (POO)

## Objetivo

En esta fase construiremos el modelo de dominio de la tienda de mascotas utilizando Programación Orientada a Objetos.

Aprenderás:

- Clases
- Objetos
- Atributos
- Constructores
- Métodos
- Encapsulación
- Sobrescritura de métodos (`toString`)
- Organización en paquetes

---

# Resultado final de la fase

Al terminar tendrás las siguientes entidades:

```text
Mascota
Cliente
Pedido
```

Y podrás crear objetos e interactuar con ellos desde la aplicación.

---

# Paso 1. Crear la carpeta de modelos

Dentro de `lib/models` crea:

```text
lib/
└── models/
    ├── mascota.dart
    ├── cliente.dart
    └── pedido.dart
```

---

# Paso 2. Crear la clase Mascota

Archivo:

```text
lib/models/mascota.dart
```

Código:

```dart
class Mascota {
  int id;
  String nombre;
  String especie;
  int edad;
  double precio;
  bool disponible;

  Mascota(
    this.id,
    this.nombre,
    this.especie,
    this.edad,
    this.precio,
    this.disponible,
  );
}
```

---

# Paso 3. Crear un objeto Mascota

En `lib/main.dart`:

```dart
import 'models/mascota.dart';

void main() {
  final mascota = Mascota(
    1,
    'Toby',
    'Perro',
    2,
    500.0,
    true,
  );

  print(mascota.nombre);
}
```

Salida:

```text
Toby
```

---

# Paso 4. Crear un método

Añadir a la clase:

```dart
void mostrarInformacion() {
  print(
    '$nombre ($especie) - $edad años - $precio €'
  );
}
```

Clase completa:

```dart
class Mascota {
  int id;
  String nombre;
  String especie;
  int edad;
  double precio;
  bool disponible;

  Mascota(
    this.id,
    this.nombre,
    this.especie,
    this.edad,
    this.precio,
    this.disponible,
  );

  void mostrarInformacion() {
    print(
      '$nombre ($especie) - $edad años - $precio €'
    );
  }
}
```

Uso:

```dart
mascota.mostrarInformacion();
```

---

# Paso 5. Sobrescribir toString()

Añadir:

```dart
@override
String toString() {
  return '$nombre ($especie)';
}
```

Ahora:

```dart
print(mascota);
```

Salida:

```text
Toby (Perro)
```

---

# Paso 6. Crear la clase Cliente

Archivo:

```text
lib/models/cliente.dart
```

Código:

```dart
class Cliente {
  int id;
  String nombre;
  String email;

  Cliente(
    this.id,
    this.nombre,
    this.email,
  );

  @override
  String toString() {
    return '$nombre - $email';
  }
}
```

---

# Paso 7. Crear la clase Pedido

Archivo:

```text
lib/models/pedido.dart
```

Código:

```dart
import 'cliente.dart';
import 'mascota.dart';

class Pedido {
  int id;
  Cliente cliente;
  Mascota mascota;
  DateTime fecha;

  Pedido(
    this.id,
    this.cliente,
    this.mascota,
    this.fecha,
  );
}
```

---

# Paso 8. Relacionar objetos

En `main.dart`:

```dart
import 'models/cliente.dart';
import 'models/mascota.dart';
import 'models/pedido.dart';

void main() {
  final mascota = Mascota(
    1,
    'Toby',
    'Perro',
    2,
    500,
    true,
  );

  final cliente = Cliente(
    1,
    'Ana López',
    'ana@email.com',
  );

  final pedido = Pedido(
    1,
    cliente,
    mascota,
    DateTime.now(),
  );

  print(cliente);
  print(mascota);
  print(pedido.fecha);
}
```

---

# Paso 9. Encapsulación

Modificar Mascota:

```dart
class Mascota {
  int _id;
  String _nombre;

  Mascota(this._id, this._nombre);

  int get id => _id;

  String get nombre => _nombre;

  set nombre(String valor) {
    if (valor.isNotEmpty) {
      _nombre = valor;
    }
  }
}
```

Conceptos aprendidos:

- Campos privados (`_`)
- Getters
- Setters
- Validación de datos

---

# Paso 10. Constructor nombrado

Añadir a Mascota:

```dart
Mascota.vacia()
    : id = 0,
      nombre = '',
      especie = '',
      edad = 0,
      precio = 0,
      disponible = false;
```

Uso:

```dart
final mascota = Mascota.vacia();
```

---

# Ejercicio práctico

Crear las siguientes mascotas:

```text
Toby - Perro - 500€
Luna - Gato - 300€
Piolín - Ave - 120€
Nemo - Pez - 25€
```

Mostrar toda la información utilizando el método:

```dart
mostrarInformacion()
```

---

# Conceptos aprendidos en esta fase

| Concepto | Uso |
|-----------|------|
| Clase | Mascota, Cliente, Pedido |
| Objeto | Instancias creadas con `new` implícito |
| Constructor | Inicialización de objetos |
| Método | mostrarInformacion() |
| Encapsulación | Getters y setters |
| Relaciones | Pedido contiene Cliente y Mascota |
| toString() | Representación personalizada |
| Organización | Carpeta models |

---

# Reto final

Implementa un método en `Pedido`:

```dart
void mostrarResumen()
```

Que muestre:

```text
===== PEDIDO =====
Cliente: Ana López
Mascota: Toby
Precio: 500.0 €
Fecha: 2026-11-06
```

Este método se reutilizará en la Fase 2, donde empezaremos a trabajar con funciones, parámetros nombrados y valores por defecto.
