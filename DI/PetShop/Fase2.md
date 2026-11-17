# Fase 2 - Funciones y Parametrización

## Objetivo

En esta fase aprenderás a utilizar funciones para encapsular lógica de negocio dentro de la tienda de mascotas.

Trabajarás con:

- Funciones
- Parámetros posicionales
- Parámetros nombrados
- Parámetros opcionales
- Valores por defecto
- Funciones flecha
- Funciones de orden superior
- Expresiones lambda

---

# Escenario

La tienda vende mascotas y productos.

Necesitamos calcular:

- Descuentos
- IVA
- Precio final
- Gastos de envío
- Búsquedas de mascotas

---

# Paso 1. Crear el servicio de ventas

Crear:

```text
lib/services/venta_service.dart
```

---

# Paso 2. Función básica

```dart
double calcularIVA(double precio) {
  return precio * 0.21;
}
```

Uso:

```dart
print(calcularIVA(100));
```

Resultado:

```text
21.0
```

---

# Paso 3. Función con varios parámetros

```dart
double calcularPrecioFinal(
  double precio,
  double descuento,
) {
  return precio - descuento;
}
```

Uso:

```dart
var total = calcularPrecioFinal(
  500,
  50,
);
```

Resultado:

```text
450
```

---

# Paso 4. Parámetros nombrados

```dart
double calcularVenta({
  required double precio,
  required double descuento,
}) {
  return precio - descuento;
}
```

Uso:

```dart
calcularVenta(
  precio: 500,
  descuento: 50,
);
```

---

# Paso 5. Valores por defecto

```dart
double calcularVenta({
  required double precio,
  double descuento = 0,
}) {
  return precio - descuento;
}
```

Uso:

```dart
calcularVenta(precio: 500);
```

Resultado:

```text
500
```

---

# Paso 6. IVA configurable

```dart
double calcularPrecioConIVA(
  double precio,
  {
    double iva = 0.21,
  }
) {
  return precio * (1 + iva);
}
```

Uso:

```dart
calcularPrecioConIVA(100);
```

Resultado:

```text
121
```

---

# Paso 7. Función flecha

```dart
double aplicarDescuento(
  double precio,
  double descuento,
) => precio - descuento;
```

---

# Paso 8. Buscar mascotas por especie

```dart
List<Mascota> buscarPorEspecie(
  List<Mascota> mascotas,
  String especie,
) {
  return mascotas
      .where((m) => m.especie == especie)
      .toList();
}
```

Uso:

```dart
var perros = buscarPorEspecie(
  mascotas,
  'Perro',
);
```

---

# Paso 9. Funciones como parámetros

```dart
double procesarPrecio(
  double precio,
  double Function(double) operacion,
) {
  return operacion(precio);
}
```

Uso:

```dart
var resultado = procesarPrecio(
  100,
  (precio) => precio * 0.9,
);
```

Resultado:

```text
90
```

---

# Paso 10. Expresiones lambda

```dart
var nombres = mascotas
    .map((m) => m.nombre)
    .toList();
```

---

# Paso 11. Crear utilidades de negocio

Archivo:

```text
lib/services/venta_service.dart
```

```dart
class VentaService {
  double calcularDescuento(
    double precio,
    {
      double porcentaje = 0,
    }
  ) {
    return precio - (precio * porcentaje);
  }

  double calcularIVA(
    double precio,
    {
      double iva = 0.21,
    }
  ) {
    return precio * (1 + iva);
  }
}
```

---

# Paso 12. Uso del servicio

```dart
final ventaService = VentaService();

var rebajado = ventaService.calcularDescuento(
  500,
  porcentaje: 0.10,
);

var finalConIVA = ventaService.calcularIVA(
  rebajado,
);

print(finalConIVA);
```

---

# Ejercicio práctico

Crear una función:

```dart
calcularEnvio()
```

Reglas:

```text
Compras < 50€  -> 5€
Compras >= 50€ -> Gratis
```

---

# Mini proyecto

Crear una lista de mascotas:

```text
Toby 500€
Luna 300€
Nemo 25€
Piolín 120€
```

Mostrar:

```text
Nombre
Precio Original
Precio con 10% descuento
Precio con IVA
```

Utilizando funciones reutilizables.

---

# Conceptos aprendidos

| Concepto | Aplicación |
|-----------|------------|
| Funciones | Cálculos de negocio |
| Parámetros | Entrada de datos |
| Named Parameters | Mayor legibilidad |
| Required | Validación de argumentos |
| Valores por defecto | IVA y descuentos |
| Arrow Functions | Operaciones simples |
| Lambdas | Filtrado y transformación |
| Funciones de orden superior | Procesamiento reutilizable |

---

# Reto final

Implementa un método:

```dart
void generarTicket()
```

Que reciba:

```dart
nombreMascota
precio
porcentajeDescuento
```

Y muestre:

```text
===== TICKET =====
Mascota: Toby
Precio original: 500 €
Descuento: 10 %
Precio final: 450 €
==================
```

La próxima fase introducirá Herencia, clases abstractas y Polimorfismo mediante los tipos de animales de la tienda.
