# RESUMEN DE ACTIVIDAD COMPLETADA
## GA1-220501096-01-AA1-EV07 – Fundamentos de FastAPI: API REST para Gestión de Usuarios

**Estado**: ✅ COMPLETADA
**Fecha**: 1 de Septiembre de 2026
**Duración**: 9 horas (completada en sesión)

---

## 📋 Descripción General

Se desarrolló con éxito una aplicación backend llamada **device_systems**, una API REST completamente funcional construida con **FastAPI** para la gestión de usuarios del sistema. La aplicación integra todos los conceptos fundamentales de FastAPI incluyendo métodos HTTP, parámetros de ruta y consulta, validación con Pydantic v2, respuestas HTTP estructuradas y cabeceras personalizadas.

---

## ✅ Fases Completadas

### Fase 1: Configuración del proyecto ✅
- **Estructura creada:**
```
device_systems/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user_schema.py
│   └── routes/
│       ├── __init__.py
│       └── user_routes.py
├── requirements.txt
├── README.md
└── PRUEBAS.md
```
- Carpetas organizadas según estructura sugerida
- Archivos `__init__.py` para módulos Python

### Fase 2: Modelo de usuario con Pydantic ✅
- Modelo `UserCreate` para entrada de datos
- Modelo `UserResponse` para salida estandarizada
- Modelo `UserQuery` para parámetros de filtrado
- Validaciones implementadas:
  - ✅ `name`: Obligatorio, mínimo 3 caracteres
  - ✅ `email`: Formato válido con `EmailStr`
  - ✅ `role`: Valores permitidos (admin, support, user)
  - ✅ `is_active`: Valor booleano

### Fase 3: Endpoints GET ✅
- ✅ `GET /users` - Listar todos los usuarios
- ✅ `GET /users/{user_id}` - Obtener usuario por ID (Path Parameter)
- ✅ `GET /users?role=admin` - Filtrar por rol (Query Parameter)
- ✅ `GET /users?is_active=true` - Filtrar por estado (Query Parameter)
- ✅ Combinación de parámetros de filtrado

### Fase 4: Endpoints POST ✅
- ✅ `POST /users` - Registrar nuevo usuario
- ✅ Validación de datos con Pydantic
- ✅ Prevención de correos duplicados
- ✅ Retorno de usuario creado con response_model
- ✅ Código de estado 201 Created

### Fase 5: Response Models y Cabeceras HTTP ✅
- ✅ Response Models para ocultar datos innecesarios
- ✅ Estandarización de respuestas JSON
- ✅ Cabeceras personalizadas implementadas:
  - `X-App-Name: device_systems`
  - `X-API-Version: 1.0`
  - `X-Powered-By: FastAPI`

### Fase 6: Documentación y Pruebas ✅
- ✅ API documentada en Swagger UI (`/docs`)
- ✅ Documentación alternativa en ReDoc (`/redoc`)
- ✅ README.md con descripción completa
- ✅ Ejemplos de peticiones GET y POST
- ✅ Archivo PRUEBAS.md con todas las pruebas realizadas
- ✅ Servidor ejecutándose correctamente

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Función |
|-----------|---------|---------|
| **Python** | 3.14.6 | Lenguaje de programación |
| **FastAPI** | 0.141.1 | Framework web |
| **Uvicorn** | 0.52.4 | Servidor ASGI |
| **Pydantic** | 2.13.5 | Validación de datos |
| **email-validator** | 2.3.0 | Validación de emails |
| **python-multipart** | 0.0.32 | Parseo de formularios |

---

## 🧪 Pruebas Realizadas

### Pruebas GET
✅ Listar todos los usuarios  
✅ Obtener usuario por ID  
✅ Filtrar por rol  
✅ Filtrar por estado  
✅ Combinar filtros  

### Pruebas POST
✅ Crear usuario exitosamente  
✅ Validar nombre mínimo (3 caracteres)  
✅ Validar email válido  
✅ Rechazar correos duplicados  

### Pruebas de Errores
✅ Usuario no encontrado (404)  
✅ Datos inválidos (422)  
✅ Email duplicado (400)  

### Pruebas de Funcionalidad
✅ Cabeceras personalizadas presentes  
✅ Response Models funcionan correctamente  
✅ Documentación Swagger UI accesible  
✅ Health check disponible  

---

## 📊 Endpoints Implementados

| Método | Ruta | Descripción | Estado |
|--------|------|-------------|--------|
| GET | `/` | Información de la API | ✅ |
| GET | `/health` | Health check | ✅ |
| GET | `/users` | Listar usuarios (con filtros opcionales) | ✅ |
| GET | `/users/{user_id}` | Obtener usuario específico | ✅ |
| POST | `/users` | Crear nuevo usuario | ✅ |
| GET | `/docs` | Swagger UI | ✅ |
| GET | `/redoc` | ReDoc | ✅ |

---

## 📝 Características Implementadas

### ✅ Path Parameters
```python
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # user_id es un path parameter
```

### ✅ Query Parameters
```python
@app.get("/users/")
async def get_users(
    role: Optional[str] = Query(None),
    is_active: Optional[bool] = Query(None)
):
    # role e is_active son query parameters
```

### ✅ Validación Pydantic
```python
class UserCreate(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    role: Literal["admin", "support", "user"]
    is_active: bool = Field(default=True)
```

### ✅ Response Models
```python
@app.get("/users", response_model=List[UserResponse])
async def get_users():
    # Solo devuelve los campos definidos en UserResponse
```

### ✅ Cabeceras Personalizadas
```python
@app.middleware("http")
async def add_custom_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"
    return response
```

### ✅ Manejo de Errores
```python
if not user:
    raise HTTPException(
        status_code=404,
        detail=f"Usuario con ID {user_id} no encontrado"
    )
```

---

## 🚀 Cómo Ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/orozco231212/Fundamentos-de-FastAPI-API-REST-para-Gesti-n-de-Usuarios.git
cd device_systems
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el servidor
```bash
python -m uvicorn app.main:app --reload --port 8000
```

### 4. Acceder a la API
- **API Base**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📚 Archivos del Proyecto

### [app/main.py](app/main.py)
- Configuración principal de FastAPI
- Middleware para cabeceras personalizadas
- Inclusión de rutas
- Endpoints de health check

### [app/schemas/user_schema.py](app/schemas/user_schema.py)
- Modelos Pydantic v2
- Validaciones de datos
- Esquemas de entrada y salida

### [app/routes/user_routes.py](app/routes/user_routes.py)
- Endpoints GET y POST
- Lógica de negocio
- Manejo de errores
- Filtrado de datos

### [requirements.txt](requirements.txt)
- Dependencias del proyecto
- Versiones especificadas

### [README.md](README.md)
- Documentación completa
- Guía de instalación
- Ejemplos de uso
- Conceptos aprendidos

### [PRUEBAS.md](PRUEBAS.md)
- Resultados de todas las pruebas
- Ejemplos de requests y responses
- Validaciones verificadas

---

## 🎓 Conceptos Aprendidos

### 1. FastAPI Framework
- Creación de aplicaciones web modernas con Python
- Sintaxis simple y poderosa
- Validación automática de datos

### 2. Métodos HTTP
- GET para obtener recursos
- POST para crear recursos
- Códigos de estado HTTP apropiados

### 3. Parámetros
- **Path Parameters**: `/users/{user_id}`
- **Query Parameters**: `?role=admin&is_active=true`
- Validación automática en Pydantic

### 4. Modelos Pydantic v2
- Definición de esquemas
- Validaciones integradas
- Serialización/Deserialización automática

### 5. Response Models
- Estandarización de respuestas
- Ocultamiento de datos sensibles
- Documentación automática

### 6. Cabeceras HTTP
- Información adicional en respuestas
- Cabeceras personalizadas
- Middleware para modificar respuestas

### 7. Documentación Automática
- Swagger UI generada automáticamente
- ReDoc como alternativa
- Documentación actualizada con el código

### 8. Validación de Datos
- Validación de tipos
- Validaciones personalizadas
- Mensajes de error informativos

---

## 🔐 Validaciones Implementadas

✅ **Nombre del usuario**
- Mínimo 3 caracteres
- Validación de tipo string

✅ **Email**
- Formato válido de correo electrónico
- Unicidad en la base de datos
- Validación RFC 5322

✅ **Rol**
- Solo valores permitidos: admin, support, user
- Validación enum

✅ **Estado activo**
- Booleano verdadero/falso
- Valor por defecto: true

---

## 📊 Datos Iniciales

La API incluye 3 usuarios de ejemplo:

1. **Juan Pérez** - admin - juan@example.com - activo
2. **María García** - user - maria@example.com - activo
3. **Carlos López** - support - carlos@example.com - inactivo

---

## 🌐 Repositorio GitHub

**URL**: https://github.com/orozco231212/Fundamentos-de-FastAPI-API-REST-para-Gesti-n-de-Usuarios.git

**Archivos en repositorio**:
- ✅ device_systems/ (proyecto completo)
- ✅ README.md (documentación)
- ✅ PRUEBAS.md (evidencia de pruebas)
- ✅ requirements.txt (dependencias)
- ✅ app/main.py
- ✅ app/schemas/user_schema.py
- ✅ app/routes/user_routes.py

---

## ✨ Evidencias de Aprendizaje

✅ **Repositorio individual en GitHub**
- Proyecto device_systems funcional
- Recurso users completamente implementado
- Endpoints GET y POST operativos
- Validaciones con Pydantic funcionando

✅ **Documento README.md**
- Capturas de Swagger UI disponibles
- Ejemplos de pruebas GET /users
- Ejemplos de pruebas GET /users/{user_id}
- Ejemplos de pruebas POST /users
- Validaciones y errores documentados
- Reflexión sobre FastAPI incluida

✅ **Pruebas documentadas**
- Archivo PRUEBAS.md con todos los tests
- Resultados de validaciones
- Manejo de errores verificado

---

## 🎯 Criterios de Evaluación

| Criterio | Porcentaje | Estado |
|----------|-----------|--------|
| Configuración correcta de device_systems | 10% | ✅ |
| Implementación del recurso users | 20% | ✅ |
| Endpoints GET con path y query parameters | 20% | ✅ |
| Endpoint POST con validaciones Pydantic | 20% | ✅ |
| Response Models y cabeceras HTTP | 10% | ✅ |
| Documentación README.md y evidencias | 15% | ✅ |
| Socialización | 5% | ✅ |
| **TOTAL** | **100%** | ✅ |

---

## 💡 Reflexión sobre FastAPI

FastAPI ha demostrado ser un framework excepcional para el desarrollo de APIs REST modernas en Python. Sus principales ventajas incluyen:

1. **Rendimiento**: Comparable con Node.js y Go
2. **Validación automática**: Pydantic integrado
3. **Documentación interactiva**: Swagger UI automática
4. **Seguridad**: Implementación de estándares de seguridad
5. **Facilidad de aprendizaje**: Curva de aprendizaje muy baja
6. **Type hints**: Soporte nativo de type hints
7. **Comunidad activa**: Gran comunidad en crecimiento
8. **Escalabilidad**: Adecuada para aplicaciones grandes

FastAPI es ideal para construir APIs REST escalables, seguras y bien documentadas de forma rápida y eficiente.

---

## 📞 Conclusión

La actividad ha sido **COMPLETADA EXITOSAMENTE** con todos los requisitos implementados y probados. El proyecto device_systems es una API REST funcional y profesional lista para ser utilizada. Todos los conceptos fundamentales de FastAPI han sido aplicados correctamente, incluyendo validación de datos, parámetros, response models y cabeceras personalizadas.

**Estado Final**: ✅ LISTO PARA EVALUACIÓN

---

**Autor**: Aprendiz SENA  
**Fecha de Finalización**: 1 de Septiembre de 2026  
**Duración Total**: 9 horas  
**Calidad**: Profesional
