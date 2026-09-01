# device_systems API REST - Gestión de Usuarios

## Descripción de la aplicación

**device_systems** es una aplicación backend desarrollada con **FastAPI** que implementa una API REST funcional para administrar usuarios del sistema. La aplicación aplica conceptos fundamentales de FastAPI incluyendo validación de datos con Pydantic v2, parámetros de ruta, parámetros de consulta, respuestas HTTP estructuradas y cabeceras personalizadas.

### Características principales:
- ✅ API REST completamente documentada con Swagger UI
- ✅ Validación de datos con Pydantic v2
- ✅ Path Parameters y Query Parameters
- ✅ Response Models para estandarizar respuestas
- ✅ Cabeceras HTTP personalizadas
- ✅ Manejo de errores HTTP
- ✅ Autenticación de datos con validadores

---

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)
- Un cliente HTTP como Postman, Thunder Client o curl

---

## Instalación de dependencias

### 1. Clonar el repositorio

```bash
git clone https://github.com/orozco231212/Fundamentos-de-FastAPI-API-REST-para-Gesti-n-de-Usuarios.git
cd device_systems
```

### 2. Crear un entorno virtual (recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución del servidor

### Opción 1: Ejecutar directamente con Python

```bash
python -m app.main
```

### Opción 2: Ejecutar con uvicorn

```bash
uvicorn app.main:app --reload
```

### Opción 3: Ejecutar en un puerto específico

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

La API estará disponible en: **http://localhost:8000**

---

## Documentación interactiva

Una vez iniciado el servidor, accede a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Tabla de Endpoints

| Método | Endpoint | Descripción | Path Params | Query Params |
|--------|----------|-------------|-------------|--------------|
| GET | `/users` | Listar todos los usuarios | - | `role`, `is_active` |
| GET | `/users/{user_id}` | Obtener un usuario por ID | `user_id` | - |
| POST | `/users` | Crear un nuevo usuario | - | - |
| GET | `/health` | Health check de la API | - | - |
| GET | `/` | Información de la API | - | - |

---

## Modelo de Usuario

### Campos obligatorios:
- **id**: Número entero único (generado automáticamente)
- **name**: Cadena de texto, mínimo 3 caracteres
- **email**: Correo electrónico válido y único
- **role**: Uno de: `admin`, `support`, `user`
- **is_active**: Booleano (true/false)

### Validaciones implementadas:
✓ El nombre debe tener mínimo 3 caracteres  
✓ El email debe ser válido  
✓ El email debe ser único en el sistema  
✓ El role debe ser uno de los valores permitidos  
✓ is_active es un valor booleano

---

## Ejemplos de peticiones

### 1. GET - Listar todos los usuarios

**Petición:**
```bash
curl http://localhost:8000/users
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "role": "admin",
    "is_active": true
  },
  {
    "id": 2,
    "name": "María García",
    "email": "maria@example.com",
    "role": "user",
    "is_active": true
  }
]
```

---

### 2. GET - Obtener usuario por ID (Path Parameter)

**Petición:**
```bash
curl http://localhost:8000/users/1
```

**Respuesta (200 OK):**
```json
{
  "id": 1,
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "role": "admin",
  "is_active": true
}
```

**Respuesta si no existe (404):**
```json
{
  "detail": "Usuario con ID 999 no encontrado"
}
```

---

### 3. GET - Filtrar usuarios por rol (Query Parameter)

**Petición:**
```bash
curl "http://localhost:8000/users?role=admin"
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "role": "admin",
    "is_active": true
  }
]
```

---

### 4. GET - Filtrar usuarios por estado activo/inactivo (Query Parameter)

**Petición:**
```bash
curl "http://localhost:8000/users?is_active=true"
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "role": "admin",
    "is_active": true
  },
  {
    "id": 2,
    "name": "María García",
    "email": "maria@example.com",
    "role": "user",
    "is_active": true
  }
]
```

---

### 5. GET - Filtrar combinando parámetros

**Petición:**
```bash
curl "http://localhost:8000/users?role=user&is_active=true"
```

**Respuesta (200 OK):**
```json
[
  {
    "id": 2,
    "name": "María García",
    "email": "maria@example.com",
    "role": "user",
    "is_active": true
  }
]
```

---

### 6. POST - Crear un nuevo usuario

**Petición:**
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Pedro Rodríguez",
    "email": "pedro@example.com",
    "role": "user",
    "is_active": true
  }'
```

**Respuesta (201 Created):**
```json
{
  "id": 4,
  "name": "Pedro Rodríguez",
  "email": "pedro@example.com",
  "role": "user",
  "is_active": true
}
```

---

### 7. POST - Error: Email duplicado

**Petición:**
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Nuevo Usuario",
    "email": "juan@example.com",
    "role": "user",
    "is_active": true
  }'
```

**Respuesta (400 Bad Request):**
```json
{
  "detail": "El email ya está registrado en el sistema"
}
```

---

### 8. POST - Error: Validación fallida

**Petición (nombre muy corto):**
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AB",
    "email": "usuario@example.com",
    "role": "user",
    "is_active": true
  }'
```

**Respuesta (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "String should have at least 3 characters",
      "type": "string_too_short"
    }
  ]
}
```

---

### 9. POST - Error: Email inválido

**Petición:**
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Usuario Nuevo",
    "email": "email-invalido",
    "role": "user",
    "is_active": true
  }'
```

**Respuesta (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address: The email address is not valid",
      "type": "value_error"
    }
  ]
}
```

---

## Cabeceras HTTP personalizadas

Cada respuesta incluye las siguientes cabeceras personalizadas:

```
X-App-Name: device_systems
X-API-Version: 1.0
X-Powered-By: FastAPI
```

---

## Estructura del proyecto

```
device_systems/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación principal
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user_schema.py   # Modelos Pydantic
│   └── routes/
│       ├── __init__.py
│       └── user_routes.py   # Endpoints de usuarios
├── requirements.txt         # Dependencias del proyecto
└── README.md               # Este archivo
```

---

## Tecnologías utilizadas

- **FastAPI**: Framework web moderno para construir APIs REST con Python
- **Pydantic v2**: Validación de datos y serialización
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Python 3.8+**: Lenguaje de programación

---

## Conceptos aprendidos

### 1. **Introducción a FastAPI**
FastAPI es un framework web moderno que facilita la construcción de APIs REST de alta calidad con validación automática y documentación interactiva.

### 2. **Métodos HTTP**
- **GET**: Obtener recursos (datos de usuarios)
- **POST**: Crear nuevos recursos (nuevo usuario)

### 3. **Path Parameters**
Se utilizan para identificar recursos específicos:
```python
@app.get("/users/{user_id}")
```

### 4. **Query Parameters**
Se utilizan para filtrar o modificar la consulta:
```python
@app.get("/users")  # ?role=admin&is_active=true
```

### 5. **Validación con Pydantic v2**
Los modelos de Pydantic validan automáticamente los datos de entrada, asegurando que cumplan con los requisitos especificados.

### 6. **Response Models**
Definen la estructura de las respuestas, ocultando datos internos innecesarios y estandarizando las respuestas de la API.

### 7. **Cabeceras HTTP**
Se utilizan para pasar información adicional entre cliente y servidor. En este caso, información sobre la aplicación y versión de la API.

### 8. **Manejo de errores**
FastAPI facilita retornar códigos de error HTTP apropiados (404, 400, 422, etc.) con mensajes descriptivos.

---

## Pruebas con herramientas

### Usando Swagger UI
1. Inicia el servidor
2. Abre http://localhost:8000/docs en tu navegador
3. Prueba todos los endpoints interactivamente

### Usando Postman
1. Crea una nueva colección
2. Importa los endpoints en Postman
3. Prueba cada endpoint con diferentes datos

### Usando Thunder Client (extensión de VS Code)
1. Instala Thunder Client en VS Code
2. Crea solicitudes HTTP
3. Prueba los endpoints directamente

### Usando curl
Consulta la sección "Ejemplos de peticiones" para comandos curl completos.

---

## Reflexión sobre FastAPI

FastAPI es una herramienta poderosa que revoluciona el desarrollo de APIs en Python. Sus principales ventajas incluyen:

1. **Validación automática**: Pydantic valida los datos automáticamente
2. **Documentación interactiva**: Swagger UI se genera automáticamente
3. **Performance**: Comparable con Node.js y Go
4. **Type hints**: Soporte nativo de type hints de Python
5. **Seguridad**: Implementación automática de seguridad
6. **Facilidad de uso**: Curva de aprendizaje baja
7. **Comunidad activa**: Comunidad grande y en crecimiento

FastAPI es ideal para construir APIs REST modernas y escalables de forma rápida y segura.

---

## Autor

Desarrollado como parte de la formación SENA en Fundamentos de FastAPI.

## Licencia

MIT

---

## Contacto

Para preguntas o sugerencias, contacta al desarrollador.
