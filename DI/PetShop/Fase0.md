# Fase 0 - Configuración inicial del proyecto PetShop con Dart y Supabase

## Objetivo

Al finalizar esta fase tendrás:

- Dart instalado y funcionando.
- Un proyecto Dart creado.
- Un proyecto en Supabase.
- Una base de datos preparada.
- La conexión entre Dart y Supabase funcionando.

---

# Paso 1. Instalar Dart SDK

Comprueba si Dart está instalado:

```bash
dart --version
```

Salida esperada:

```text
Dart SDK version: 3.x.x
```

Si no está instalado:

### Windows (Chocolatey)

```powershell
choco install dart-sdk
```

Verifica nuevamente:

```bash
dart --version
```

---

# Paso 2. Crear el proyecto

```bash
dart create petshop
```

Entrar en la carpeta:

```bash
cd petshop
```

Ejecutar:

```bash
dart run
```

Resultado esperado:

```text
Hello world!
```

---

# Paso 3. Crear la estructura inicial

Dentro de `lib/` crea la siguiente estructura:

```text
lib/
│
├── models/
├── repositories/
├── services/
├── database/
├── extensions/
├── generators/
└── main.dart
```

En Linux o WSL:

```bash
mkdir lib/models
mkdir lib/repositories
mkdir lib/services
mkdir lib/database
mkdir lib/extensions
mkdir lib/generators
```

---

# Paso 4. Crear cuenta en Supabase

Accede a:

https://supabase.com

Crea una cuenta utilizando:

- GitHub
- Google
- Correo electrónico

---

# Paso 5. Crear el proyecto Supabase

Selecciona:

```text
New Project
```

Configuración sugerida:

```text
Name: petshop
Database Password: contraseña_segura
Region: Europe West
```

Espera a que el proyecto termine de desplegarse.

---

# Paso 6. Obtener URL y API Key

En Supabase:

```text
Project Settings
↓
API
```

Guarda:

```text
Project URL
Anon Public Key
```

Ejemplo:

```text
https://abcdefgh.supabase.co

eyJhbGc...
```

---

# Paso 7. Instalar el paquete Supabase

Desde la carpeta del proyecto:

```bash
dart pub add supabase
```

Actualizar dependencias:

```bash
dart pub get
```

Comprobar que aparece en `pubspec.yaml`:

```yaml
dependencies:
  supabase: ^2.x.x
```

---

# Paso 8. Crear la configuración de conexión

Archivo:

```text
lib/database/supabase_client.dart
```

Contenido:

```dart
import 'package:supabase/supabase.dart';

class DatabaseConfig {
  static const url = 'TU_URL';

  static const anonKey = 'TU_API_KEY';

  static final client = SupabaseClient(
    url,
    anonKey,
  );
}
```

> No subas claves reales a GitHub.

---

# Paso 9. Crear la tabla mascotas

Abrir:

```text
SQL Editor
↓
New Query
```

Ejecutar:

```sql
create table mascotas (
    id bigint generated always as identity primary key,
    nombre text not null,
    especie text not null,
    edad integer not null,
    precio numeric(10,2) not null,
    disponible boolean default true
);
```

---

# Paso 10. Insertar datos de prueba

```sql
insert into mascotas
(nombre, especie, edad, precio)
values
('Toby','Perro',2,500),
('Luna','Gato',1,300),
('Nemo','Pez',1,25);
```

---

# Paso 11. Probar la conexión desde Dart

Archivo:

```text
bin/petshop.dart
```

Código:

```dart
import 'package:supabase/supabase.dart';

void main() async {
 
  var supabase = DatabaseConfig.client;

  final mascotas = await supabase
      .from('mascotas')
      .select();

  print(mascotas);
}
```

Ejecutar:

```bash
dart run
```

Salida esperada:

```text
[
  {id: 1, nombre: Toby, especie: Perro},
  {id: 2, nombre: Luna, especie: Gato},
  {id: 3, nombre: Nemo, especie: Pez}
]
```

---

# Paso 12. Configurar permisos (RLS)

Si aparece un error de permisos:

```text
permission denied
```

Ejecuta:

```sql
alter table mascotas
enable row level security;
```

Crear política de lectura:

```sql
create policy "lectura_publica"
on mascotas
for select
using (true);
```

---

# Conceptos de Dart vistos en esta fase

## Variables

```dart
const url = '...';
```

## Objetos

```dart
final supabase = SupabaseClient(...);
```

## Métodos

```dart
.from('mascotas')
.select();
```

## Future

```dart
await consulta();
```

## Async

```dart
void main() async {}
```

## Colecciones

La consulta devuelve una colección de resultados.

---

# Reto final

Muestra las mascotas con un bucle `for`:

```text
=== MASCOTAS DISPONIBLES ===

Toby - Perro
Luna - Gato
Nemo - Pez
```

Usa los datos obtenidos desde Supabase y recorre la lista para imprimir cada mascota.
