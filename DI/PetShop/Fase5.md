# Fase 5 - Null Safety en Dart

## Objetivo

En esta fase aprenderás a trabajar de forma segura con valores que pueden ser nulos.

Null Safety es una de las características más importantes de Dart porque ayuda a evitar errores en tiempo de ejecución.

Aprenderás:

- Tipos anulables (`?`)
- Operador `??`
- Operador `?.`
- Operador `!`
- `late`
- Variables opcionales
- Casos reales aplicados a la tienda de mascotas

---

# Escenario

En una tienda de mascotas no todos los clientes tienen la misma información.

Por ejemplo:

```text
Nombre → Obligatorio
Email → Obligatorio
Teléfono → Opcional
Observaciones → Opcional
Dirección → Opcional
```

---

# Paso 1. Variables no nulas

```dart
String nombre = 'Ana';
```

Correcto:

```dart
nombre = 'María';
```

Incorrecto:

```dart
nombre = null;
```

Dart mostrará un error de compilación.

---

# Paso 2. Tipos anulables

```dart
String? telefono;
```

Ahora sí es válido:

```dart
telefono = null;
```

Y también:

```dart
telefono = '600123123';
```

---

# Paso 3. Cliente con campos opcionales

```dart
class Cliente {
  int id;
  String nombre;
  String email;
  String? telefono;
  String? direccion;

  Cliente(
    this.id,
    this.nombre,
    this.email,
    this.telefono,
    this.direccion,
  );
}
```

---

# Paso 4. El problema del null

```dart
print(cliente.telefono.length);
```

Error:

```text
The property 'length' can't be unconditionally accessed
```

Porque podría ser null.

---

# Paso 5. Operador ?.

Acceso seguro:

```dart
print(cliente.telefono?.length);
```

Si el teléfono es null:

```text
null
```

No se produce ninguna excepción.

---

# Paso 6. Operador ??

Proporcionar un valor alternativo.

```dart
print(
  cliente.telefono ?? 'Sin teléfono'
);
```

Resultado:

```text
Sin teléfono
```

---

# Paso 7. Operador ??=

Asignar solo cuando el valor es nulo.

```dart
cliente.telefono ??= 'No disponible';
```

---

# Paso 8. Operador !

Indica que estamos seguros de que el valor no es null.

```dart
print(cliente.telefono!);
```

Usar únicamente cuando exista una garantía real.

---

# Paso 9. Propiedad observaciones

```dart
class Mascota {
  int id;
  String nombre;
  String especie;
  String? observaciones;

  Mascota(
    this.id,
    this.nombre,
    this.especie,
    this.observaciones,
  );
}
```

Uso:

```dart
print(
  mascota.observaciones ??
  'Sin observaciones'
);
```

---

# Paso 10. Null Safety con listas

```dart
List<String>? vacunas;
```

Comprobar:

```dart
print(vacunas?.length);
```

---

# Paso 11. Utilizar late

Algunas variables se inicializan posteriormente.

```dart
late String apiKey;
```

Más tarde:

```dart
apiKey = 'abc123';
```

---

# Paso 12. Caso práctico Supabase

```dart
late final SupabaseClient supabase;
```

Inicialización:

```dart
supabase = SupabaseClient(
  url,
  anonKey,
);
```

---

# Paso 13. Modelo completo de Cliente

```dart
class Cliente {
  int id;
  String nombre;
  String email;
  String? telefono;
  String? direccion;
  String? observaciones;

  Cliente(
    this.id,
    this.nombre,
    this.email,
    this.telefono,
    this.direccion,
    this.observaciones,
  );
}
```

---

# Paso 14. Mostrar datos de forma segura

```dart
void mostrarCliente(
  Cliente cliente,
) {
  print('Nombre: ${cliente.nombre}');

  print(
    'Teléfono: '
    '${cliente.telefono ?? "No disponible"}'
  );

  print(
    'Dirección: '
    '${cliente.direccion ?? "No indicada"}'
  );
}
```

---

# Ejercicio práctico

Crear tres clientes:

```text
Cliente 1 → teléfono y dirección
Cliente 2 → solo teléfono
Cliente 3 → sin teléfono ni dirección
```

Mostrar los datos utilizando `??`.

---

# Mini proyecto

Crear una lista de mascotas donde algunas tengan observaciones y otras no.

Mostrar:

```text
Nombre
Especie
Observaciones
```

Si no existen observaciones:

```text
Sin observaciones
```

---

# Conceptos aprendidos

| Concepto | Uso |
|-----------|------|
| ? | Tipo anulable |
| ?. | Acceso seguro |
| ?? | Valor alternativo |
| ??= | Asignación condicional |
| ! | Forzar valor no nulo |
| late | Inicialización tardía |
| Null Safety | Prevención de errores |

---

# Reto final

Implementa una clase:

```dart
Pedido
```

Con los campos:

```dart
id
cliente
mascota
comentarios
fechaEntrega
```

Donde:

```text
comentarios → opcional
fechaEntrega → opcional
```

Crea un método que muestre toda la información usando correctamente:

- ?.
- ??
- tipos anulables

