"""Endpoints REST para la gestión de usuarios."""

from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.user_schema import UserCreate, UserResponse, UserRole

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Usuario no encontrado"}},
)

users_db: list[dict] = [
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

next_id = 4


@router.get("", response_model=list[UserResponse], summary="Listar usuarios")
async def get_users(
    role: Annotated[UserRole | None, Query(description="Filtrar por rol")] = None,
    is_active: Annotated[bool | None, Query(description="Filtrar por estado")] = None,
) -> list[dict]:
    """
    Obtiene la lista de todos los usuarios con opciones de filtrado.
    
    - **role**: Filtrar por rol (admin, support, user)
    - **is_active**: Filtrar por estado (true/false)
    """
    result = users_db.copy()

    if role is not None:
        result = [user for user in result if user["role"] == role.value]

    if is_active is not None:
        result = [user for user in result if user["is_active"] == is_active]

    return result


@router.get("/{user_id}", response_model=UserResponse, summary="Obtener usuario por ID")
async def get_user(user_id: int) -> dict:
    """
    Obtiene un usuario específico por su ID.
    
    - **user_id**: ID único del usuario (Path Parameter)
    """
    user = next((u for u in users_db if u["id"] == user_id), None)
    
    if user is None:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario con ID {user_id} no encontrado"
        )
    
    return user


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED, summary="Crear usuario")
async def create_user(user: UserCreate) -> dict:
    """
    Crea un nuevo usuario en el sistema.
    
    Validaciones:
    - El nombre debe tener mínimo 3 caracteres
    - El email debe ser válido y único
    - El role debe ser uno de: admin, support, user
    - is_active es booleano
    """
    global next_id
    
    if any(existing_user["email"] == str(user.email) for existing_user in users_db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El email ya está registrado en el sistema"
        )
    
    new_user = {
        "id": next_id,
        "name": user.name,
        "email": str(user.email),
        "role": user.role.value,
        "is_active": user.is_active
    }
    
    users_db.append(new_user)
    next_id += 1
    
    return new_user
