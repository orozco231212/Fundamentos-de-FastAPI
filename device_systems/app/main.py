"""
Aplicación principal de FastAPI para device_systems
API REST para gestión de usuarios
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.user_routes import router as users_router

# Crear instancia de FastAPI
app = FastAPI(
    title="device_systems API",
    description="API REST para la gestión de usuarios del sistema device_systems",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir las rutas de usuarios
app.include_router(users_router)


@app.get("/", summary="Raíz de la API")
async def root():
    """Endpoint raíz que devuelve información sobre la API"""
    return {
        "message": "Bienvenido a device_systems API",
        "version": "1.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", summary="Health Check")
async def health_check():
    """Verifica que la API esté disponible"""
    return {"status": "ok", "service": "device_systems"}


# Middleware para agregar cabeceras personalizadas
@app.middleware("http")
async def add_custom_headers(request, call_next):
    """Middleware que agrega cabeceras HTTP personalizadas"""
    response = await call_next(request)
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"
    response.headers["X-Powered-By"] = "FastAPI"
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
