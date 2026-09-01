"""
Schemas de Pydantic v2 para validación de datos de usuarios
"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal


class UserCreate(BaseModel):
    """Esquema para crear un nuevo usuario"""
    name: str = Field(..., min_length=3, description="Nombre del usuario (mínimo 3 caracteres)")
    email: EmailStr = Field(..., description="Email válido del usuario")
    role: Literal["admin", "support", "user"] = Field(..., description="Rol del usuario")
    is_active: bool = Field(default=True, description="Estado del usuario")


class UserResponse(BaseModel):
    """Esquema de respuesta para usuarios"""
    id: int = Field(..., description="ID único del usuario")
    name: str = Field(..., description="Nombre del usuario")
    email: EmailStr = Field(..., description="Email del usuario")
    role: str = Field(..., description="Rol del usuario")
    is_active: bool = Field(..., description="Estado del usuario")

    class Config:
        from_attributes = True


class UserQuery(BaseModel):
    """Esquema para parámetros de consulta"""
    role: Optional[Literal["admin", "support", "user"]] = Field(None, description="Filtrar por rol")
    is_active: Optional[bool] = Field(None, description="Filtrar por estado activo/inactivo")
