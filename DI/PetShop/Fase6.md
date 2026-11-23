# Fase 6 - Extensions en Dart

## Objetivo

Las Extensions permiten añadir funcionalidades a clases existentes sin modificar su código original.

En esta fase aprenderás:

- Crear Extensions
- Extender clases del SDK de Dart
- Extender tus propias clases
- Reutilizar lógica de negocio
- Mejorar la legibilidad del código

---

# Escenario

En nuestra tienda de mascotas queremos:

- Formatear precios
- Formatear fechas
- Formatear nombres
- Añadir utilidades a Mascota

Sin modificar directamente las clases originales.

---

# Paso 1. Primera Extension

Crear:

```text
lib/extensions/precio_extension.dart
```

```dart
extension PrecioExtension on double {
  String toEuro() {
    return '${toStringAsFixed(2)} €';
  }
}
```

Uso:

```dart
print(25.5.toEuro());
```

Resultado:

```text
25.50 €
```

---

# Paso 2. Utilizar la extensión en Mascota

```dart
print(mascota.precio.toEuro());
```

---

# Paso 3. Extension para String

```dart
extension NombreExtension on String {
  String capitalizar() {
    return isEmpty
        ? this
        : this[0].toUpperCase() + substring(1);
  }
}
```

Uso:

```dart
print('toby'.capitalizar());
```

Resultado:

```text
Toby
```

---

# Paso 4. Extension para DateTime

```dart
extension FechaExtension on DateTime {
  String formatoSimple() {
    return '$day/$month/$year';
  }
}
```

Uso:

```dart
print(DateTime.now().formatoSimple());
```

---

# Paso 5. Extension sobre Mascota

Crear:

```text
lib/extensions/mascota_extension.dart
```

```dart
import '../models/mascota.dart';

extension MascotaExtension on Mascota {
  bool esCara() {
    return precio >= 300;
  }
}
```

Uso:

```dart
print(mascota.esCara());
```

---

# Paso 6. Varias utilidades

```dart
extension MascotaExtension on Mascota {
  bool esCara() => precio >= 300;

  bool esEconomica() => precio < 100;

  String resumen() {
    return '$nombre - $especie - $precio €';
  }
}
```

---

# Paso 7. Encadenar extensiones

```dart
print(
  mascota.nombre.capitalizar()
);
```

```dart
print(
  mascota.precio.toEuro()
);
```

---

# Paso 8. Extension para descuentos

```dart
extension DescuentoExtension on double {
  double aplicarDescuento(
    double porcentaje,
  ) {
    return this - (this * porcentaje);
  }
}
```

Uso:

```dart
print(
  500.0.aplicarDescuento(0.10)
);
```

Resultado:

```text
450
```

---

# Paso 9. Catálogo mejorado

```dart
for (final mascota in catalogo) {
  print(
    mascota.resumen()
  );
}
```

Salida:

```text
Toby - Perro - 500 €
Luna - Gato - 300 €
Nemo - Pez - 25 €
```

---

# Paso 10. Agrupar extensions

```text
lib/extensions/
├── precio_extension.dart
├── fecha_extension.dart
├── string_extension.dart
└── mascota_extension.dart
```

---

# Ejercicio práctico

Crear una extensión sobre String:

```dart
ocultarEmail()
```

Ejemplo:

```text
ana@email.com
```

Resultado:

```text
a***@email.com
```

---

# Mini proyecto

Crear extensiones para:

- Precio
- Nombre
- Fecha
- Mascota

Mostrar un catálogo completo utilizando únicamente métodos añadidos mediante extensions.

---

# Conceptos aprendidos

| Concepto | Uso |
|-----------|------|
| extension | Ampliar funcionalidades |
| on | Tipo extendido |
| Reutilización | Evitar duplicar código |
| Encadenamiento | Varias extensiones juntas |
| Legibilidad | Código más expresivo |

---

# Reto final

Implementa las siguientes extensiones:

```dart
double.toEuro()
double.aplicarIVA()
double.aplicarDescuento()
String.capitalizar()
DateTime.formatoSimple()
Mascota.resumen()
```

Después crea un listado como:

```text
===== CATÁLOGO =====
Toby - Perro - 500.00 €
Luna - Gato - 300.00 €
Nemo - Pez - 25.00 €
```

Utilizando exclusivamente métodos proporcionados por Extensions.

