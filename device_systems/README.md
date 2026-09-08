# device_systems

API REST para la gestión de usuarios, construida con FastAPI y Pydantic v2 para la evidencia GA1-220501096-01-AA1-EV07.

## Requisitos

- Python 3.10 o superior
- pip
- Postman, Thunder Client o curl

## Instalación y ejecución en Windows

Después de clonar el repositorio, entra a la carpeta del proyecto:

```powershell
git clone https://github.com/orozco231212/Fundamentos-de-FastAPI-API-REST-para-Gesti-n-de-Usuarios.git
cd Fundamentos-de-FastAPI-API-REST-para-Gesti-n-de-Usuarios\device_systems
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Si PowerShell bloquea la activación del entorno, ejecuta el servidor directamente:

```powershell
.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`.

Documentación interactiva:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Para detener el servidor: `Ctrl+C`.

## Estructura

```text
device_systems/
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── user_routes.py
│   └── schemas/
│       └── user_schema.py
├── tests/
│   └── test_users.py
├── .gitignore
├── requirements.txt
└── README.md
```

La información se almacena temporalmente en memoria. Al reiniciar el servidor, los usuarios creados mediante POST se reinician.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Información general de la API |
| GET | `/health` | Estado del servicio |
| GET | `/users` | Lista todos los usuarios |
| GET | `/users/{user_id}` | Consulta un usuario por ID |
| GET | `/users?role=admin` | Filtra por rol |
| GET | `/users?is_active=true` | Filtra por estado |
| POST | `/users` | Registra un usuario |

Todas las respuestas incluyen `X-App-Name: device_systems` y `X-API-Version: 1.0`.

## Modelo y validaciones

El cuerpo de `POST /users` acepta:

```json
{
  "name": "Ana Torres",
  "email": "ana.torres@example.com",
  "role": "support",
  "is_active": true
}
```

- `name` es obligatorio y debe tener mínimo 3 caracteres.
- `email` debe tener formato válido y no repetirse.
- `role` solo acepta `admin`, `support` o `user`.
- `is_active` es booleano y por defecto vale `true`.
- `id` se genera automáticamente y se entrega mediante `UserResponse`.

## Pruebas rápidas

```powershell
curl http://127.0.0.1:8000/users
curl http://127.0.0.1:8000/users/1
curl "http://127.0.0.1:8000/users?role=admin&is_active=true"
curl -X POST http://127.0.0.1:8000/users -H "Content-Type: application/json" -d '{"name":"Ana Torres","email":"ana.torres@example.com","role":"support","is_active":true}'
```

Ejecutar la suite automatizada desde la carpeta del repositorio:

```powershell
.venv\Scripts\python.exe -m pytest tests -q
```

Casos cubiertos: listado y cabeceras, filtros, búsqueda por ID, creación, rechazo de correo duplicado y validación de nombre corto.

## Organizar y subir cambios a GitHub

Ejecuta estos comandos desde la carpeta raíz del repositorio, donde está `device_systems`:

```powershell
git status
git add device_systems
git commit -m "Completar API REST de usuarios con FastAPI"
git push origin main
```

Antes del `commit`, revisa `git status` y confirma que no aparezcan `.venv`, `__pycache__` ni `.pytest_cache`. Esos archivos están excluidos mediante `.gitignore` y no deben subirse.

## Respuestas de error

- `404`: usuario inexistente.
- `409`: correo ya registrado.
- `422`: datos que no cumplen el modelo Pydantic.

## Evidencias para la entrega

En Swagger UI, ejecutar y capturar:

1. `GET /users`.
2. `GET /users/{user_id}` con un ID existente y otro inexistente.
3. `GET /users` usando `role` e `is_active`.
4. `POST /users` exitoso.
5. `POST /users` con correo duplicado y datos inválidos.

## Reflexión

FastAPI permite declarar rutas, parámetros y modelos de validación en un código breve. Pydantic verifica automáticamente la entrada y FastAPI genera Swagger UI a partir de esas declaraciones, lo que facilita probar y documentar la API durante el desarrollo.
