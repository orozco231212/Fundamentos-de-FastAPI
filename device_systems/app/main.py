"""Punto de entrada de la API REST device_systems."""

from fastapi import FastAPI, Request
from app.routes.user_routes import router as users_router

app = FastAPI(
    title="device_systems API",
    description="API REST para la gestión de usuarios del sistema device_systems",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(users_router)


@app.get("/", summary="Información de la API")
async def root() -> dict[str, str]:
    return {
        "message": "Bienvenido a device_systems API",
        "version": "1.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", summary="Comprobar disponibilidad")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "service": "device_systems"}


@app.middleware("http")
async def add_custom_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"
    return response



