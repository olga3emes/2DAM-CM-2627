# Fase 4 - Colecciones en Dart (List, Set y Map)

## Objetivo

En esta fase aprenderás a utilizar las colecciones más importantes de Dart para gestionar la información de la tienda de mascotas.

Trabajarás con:

- List
- Set
- Map
- Recorridos
- Filtrado
- Transformación de datos
- Ordenación
- Operaciones avanzadas sobre colecciones

---

# Escenario

Nuestra tienda ya tiene mascotas, clientes y pedidos.

Ahora necesitamos almacenar:

- Catálogo de mascotas
- Categorías de animales
- Stock de productos
- Clientes registrados

---

# Paso 1. Trabajar con List

Las listas permiten almacenar varios elementos en orden.

```dart
List<String> mascotas = [
  'Toby',
  'Luna',
  'Nemo',
];
```

Mostrar contenido:

```dart
print(mascotas);
```

---

# Paso 2. Añadir elementos

```dart
mascotas.add('Piolín');
```

Resultado:

```text
[Toby, Luna, Nemo, Piolín]
```

---

# Paso 3. Eliminar elementos

```dart
mascotas.remove('Nemo');
```

---

# Paso 4. Recorrer una lista

```dart
for (final mascota in mascotas) {
  print(mascota);
}
```

---

# Paso 5. Lista de objetos

```dart
List<Mascota> catalogo = [
  Mascota(1, 'Toby', 'Perro', 2, 500, true),
  Mascota(2, 'Luna', 'Gato', 1, 300, true),
  Mascota(3, 'Nemo', 'Pez', 1, 25, true),
];
```

---

# Paso 6. Buscar elementos

```dart
var perro = catalogo.firstWhere(
  (m) => m.nombre == 'Toby',
);
```

---

# Paso 7. Filtrar elementos

```dart
var perros = catalogo.where(
  (m) => m.especie == 'Perro',
).toList();
```

---

# Paso 8. Transformar datos con map()

```dart
var nombres = catalogo
    .map((m) => m.nombre)
    .toList();
```

Resultado:

```text
[Toby, Luna, Nemo]
```

---

# Paso 9. Ordenar colecciones

```dart
catalogo.sort(
  (a, b) => a.precio.compareTo(b.precio),
);
```

---

# Paso 10. Introducción a Set

Un Set no permite elementos repetidos.

```dart
Set<String> categorias = {
  'Perro',
  'Gato',
  'Pez',
};
```

---

# Paso 11. Evitar duplicados

```dart
categorias.add('Perro');
```

Resultado:

```text
{Perro, Gato, Pez}
```

No se inserta de nuevo.

---

# Paso 12. Recorrer un Set

```dart
for (final categoria in categorias) {
  print(categoria);
}
```

---

# Paso 13. Introducción a Map

Un Map almacena parejas clave-valor.

```dart
Map<String, int> stock = {
  'Pienso': 50,
  'Juguete': 30,
  'Correa': 15,
};
```

---

# Paso 14. Acceder a valores

```dart
print(stock['Pienso']);
```

Resultado:

```text
50
```

---

# Paso 15. Modificar valores

```dart
stock['Pienso'] = 40;
```

---

# Paso 16. Añadir productos

```dart
stock['Jaula'] = 10;
```

---

# Paso 17. Recorrer un Map

```dart
stock.forEach((producto, cantidad) {
  print('$producto -> $cantidad');
});
```

---

# Paso 18. Operaciones útiles

Comprobar existencia:

```dart
stock.containsKey('Pienso');
```

Cantidad disponible:

```dart
stock.containsValue(50);
```

---

# Paso 19. any() y every()

Existe alguna mascota cara:

```dart
catalogo.any(
  (m) => m.precio > 400,
);
```

Todas disponibles:

```dart
catalogo.every(
  (m) => m.disponible,
);
```

---

# Paso 20. Calcular totales con fold()

```dart
var total = catalogo.fold<double>(
  0,
  (acumulado, mascota) =>
      acumulado + mascota.precio,
);
```

---

# Caso práctico: Inventario completo

```dart
List<Mascota> inventario = [
  Mascota(1, 'Toby', 'Perro', 2, 500, true),
  Mascota(2, 'Luna', 'Gato', 1, 300, true),
  Mascota(3, 'Nemo', 'Pez', 1, 25, true),
  Mascota(4, 'Piolín', 'Ave', 1, 120, true),
];
```

Mostrar:

```text
Nombre
Especie
Precio
```

Utilizando un bucle.

---

# Ejercicio práctico

Crear un Map de productos:

```text
Pienso -> 50
Correa -> 15
Jaula -> 10
Juguete -> 30
```

Mostrar únicamente aquellos con stock inferior a 20 unidades.

---

# Conceptos aprendidos

| Concepto | Uso |
|-----------|------|
| List | Catálogo de mascotas |
| Set | Categorías únicas |
| Map | Stock de productos |
| where | Filtrado |
| map | Transformación |
| sort | Ordenación |
| any | Comprobaciones |
| every | Validaciones |
| fold | Acumulación |

---

# Reto final

Construye un sistema que:

1. Guarde las mascotas en una lista.
2. Obtenga todas las categorías mediante un Set.
3. Mantenga el stock mediante un Map.
4. Calcule el valor total del catálogo usando fold().
5. Muestre las mascotas ordenadas por precio.

La siguiente fase introducirá Null Safety, operadores ?, ??, ! y ?. para trabajar de forma segura con valores opcionales.
