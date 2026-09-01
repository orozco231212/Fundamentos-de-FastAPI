"""
Rutas para la gestión de usuarios
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional, Literal
from ..schemas import UserCreate, UserResponse, UserQuery

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Usuario no encontrado"}},
)

# Base de datos simulada en memoria
users_db: List[dict] = [
    {
        "id": 1,
        "name": "Juan Pérez",
        "email": "juan@example.com",
        "role": "admin",
        "is_active": True
    },
    {
        "id": 2,
        "name": "María García",
        "email": "maria@example.com",
        "role": "user",
        "is_active": True
    },
    {
        "id": 3,
        "name": "Carlos López",
        "email": "carlos@example.com",
        "role": "support",
        "is_active": False
    }
]

# Contador para IDs
next_id = 4


@router.get("/", response_model=List[UserResponse], summary="Listar todos los usuarios")
async def get_users(
    role: Optional[Literal["admin", "support", "user"]] = Query(None, description="Filtrar por rol"),
    is_active: Optional[bool] = Query(None, description="Filtrar por estado activo/inactivo")
):
    """
    Obtiene la lista de todos los usuarios con opciones de filtrado.
    
    - **role**: Filtrar por rol (admin, support, user)
    - **is_active**: Filtrar por estado (true/false)
    """
    result = users_db.copy()
    
    if role:
        result = [u for u in result if u["role"] == role]
    
    if is_active is not None:
        result = [u for u in result if u["is_active"] == is_active]
    
    return result


@router.get("/{user_id}", response_model=UserResponse, summary="Obtener usuario por ID")
async def get_user(user_id: int):
    """
    Obtiene un usuario específico por su ID.
    
    - **user_id**: ID único del usuario (Path Parameter)
    """
    user = next((u for u in users_db if u["id"] == user_id), None)
    
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario con ID {user_id} no encontrado"
        )
    
    return user


@router.post("/", response_model=UserResponse, status_code=201, summary="Crear nuevo usuario")
async def create_user(user: UserCreate):
    """
    Crea un nuevo usuario en el sistema.
    
    Validaciones:
    - El nombre debe tener mínimo 3 caracteres
    - El email debe ser válido y único
    - El role debe ser uno de: admin, support, user
    - is_active es booleano
    """
    global next_id
    
    # Validar que el email no exista
    if any(u["email"] == user.email for u in users_db):
        raise HTTPException(
            status_code=400,
            detail="El email ya está registrado en el sistema"
        )
    
    # Crear nuevo usuario
    new_user = {
        "id": next_id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active
    }
    
    users_db.append(new_user)
    next_id += 1
    
    return new_user
