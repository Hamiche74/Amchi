from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from app.core.config import settings
from app.core.logger import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Lifespan context manager for startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("🚀 Starting Amchi Payment Gateway API...")
    yield
    # Shutdown
    logger.info("🛑 Shutting down Amchi Payment Gateway API...")

# Create FastAPI instance
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/api/docs" if settings.DEBUG else None,
    redoc_url="/api/redoc" if settings.DEBUG else None,
    openapi_url="/api/openapi.json" if settings.DEBUG else None,
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check Endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint to verify API is running"""
    return {
        "status": "healthy",
        "service": settings.API_TITLE,
        "version": settings.API_VERSION,
        "environment": settings.ENVIRONMENT
    }

# Root Endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Amchi Payment Gateway API",
        "version": settings.API_VERSION,
        "docs": "/api/docs",
        "status": "operational"
    }

# Include routers (will be added later)
# from app.api.v1 import api_router
# app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )