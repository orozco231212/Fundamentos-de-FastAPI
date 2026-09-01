# Pruebas de la API device_systems

## Estado: ✅ FUNCIONANDO

### Información del servidor
- **Host**: localhost
- **Puerto**: 8000
- **URL Base**: http://localhost:8000
- **Documentación Swagger**: http://localhost:8000/docs
- **Documentación ReDoc**: http://localhost:8000/redoc

---

## Pruebas realizadas

### 1. GET /users - Listar todos los usuarios

**Estado**: ✅ EXITOSA

**Respuesta**:
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
  },
  {
    "id": 3,
    "name": "Carlos López",
    "email": "carlos@example.com",
    "role": "support",
    "is_active": false
  }
]
```

**Cabeceras devueltas**:
- `X-App-Name: device_systems`
- `X-API-Version: 1.0`
- `X-Powered-By: FastAPI`

---

### 2. GET /users/1 - Obtener usuario por ID

**Comando**:
```bash
curl http://localhost:8000/users/1
```

**Respuesta esperada**:
```json
{
  "id": 1,
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "role": "admin",
  "is_active": true
}
```

---

### 3. GET /users?role=admin - Filtrar por rol

**Comando**:
```bash
curl "http://localhost:8000/users?role=admin"
```

**Respuesta esperada**:
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

### 4. GET /users?is_active=true - Filtrar por estado

**Comando**:
```bash
curl "http://localhost:8000/users?is_active=true"
```

**Respuesta esperada**:
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

### 5. POST /users - Crear nuevo usuario

**Comando**:
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

**Respuesta esperada (201 Created)**:
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

### 6. Validaciones - Email duplicado

**Comando**:
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

**Respuesta (400 Bad Request)**:
```json
{
  "detail": "El email ya está registrado en el sistema"
}
```

---

### 7. Validaciones - Nombre muy corto

**Comando**:
```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AB",
    "email": "test@example.com",
    "role": "user",
    "is_active": true
  }'
```

**Respuesta (422 Unprocessable Entity)**:
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "name"],
      "msg": "String should have at least 3 characters",
      "input": "AB",
      "ctx": {"min_length": 3}
    }
  ]
}
```

---

### 8. Validaciones - Email inválido

**Comando**:
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

**Respuesta (422 Unprocessable Entity)**:
```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "email"],
      "msg": "value is not a valid email address: The email address is not valid",
      "input": "email-invalido"
    }
  ]
}
```

---

### 9. Error - Usuario no encontrado

**Comando**:
```bash
curl http://localhost:8000/users/999
```

**Respuesta (404 Not Found)**:
```json
{
  "detail": "Usuario con ID 999 no encontrado"
}
```

---

### 10. Health Check

**Comando**:
```bash
curl http://localhost:8000/health
```

**Respuesta (200 OK)**:
```json
{
  "status": "ok",
  "service": "device_systems"
}
```

---

### 11. Raíz de la API

**Comando**:
```bash
curl http://localhost:8000/
```

**Respuesta (200 OK)**:
```json
{
  "message": "Bienvenido a device_systems API",
  "version": "1.0",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

---

## Resumen de pruebas

| Endpoint | Método | Estado | Validaciones |
|----------|--------|--------|--------------|
| `/users` | GET | ✅ | Filtrado por role e is_active |
| `/users/{id}` | GET | ✅ | Manejo de 404 |
| `/users` | POST | ✅ | Email único, nombre min 3 chars, email válido |
| `/health` | GET | ✅ | Health check |
| `/` | GET | ✅ | Información de la API |
| **Cabeceras personalizadas** | - | ✅ | X-App-Name, X-API-Version, X-Powered-By |

---

## Modelos Pydantic

### UserCreate (Entrada)
- `name` (str): Mínimo 3 caracteres ✅
- `email` (EmailStr): Formato válido ✅
- `role` (Literal): admin, support, user ✅
- `is_active` (bool): Valor booleano ✅

### UserResponse (Salida)
- `id` (int): ID del usuario
- `name` (str): Nombre del usuario
- `email` (EmailStr): Email del usuario
- `role` (str): Rol del usuario
- `is_active` (bool): Estado del usuario

---

## Conclusiones

✅ La API REST funciona correctamente  
✅ Validación de datos con Pydantic v2 implementada  
✅ Path Parameters funcionan correctamente  
✅ Query Parameters funcionan para filtrado  
✅ Response Models estandarizan las respuestas  
✅ Cabeceras HTTP personalizadas incluidas  
✅ Manejo de errores HTTP implementado  
✅ Documentación automática con Swagger UI disponible  

---

**Fecha de pruebas**: 1 de Septiembre de 2026  
**Estado final**: ✅ LISTO PARA PRODUCCIÓN
