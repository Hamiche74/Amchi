from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    This is the central configuration for the entire Amchi Payment Gateway.
    """
    
    # ============================================
    # API CONFIGURATION
    # ============================================
    API_TITLE: str = "Amchi Payment Gateway"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "A payment gateway solution adapted to Niger and Africa's populations"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1", "0.0.0.0"]
    
    # ============================================
    # DATABASE CONFIGURATION
    # ============================================
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/amchi_db"
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 0
    
    # ============================================
    # JWT & SECURITY
    # ============================================
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # ============================================
    # ORANGE MONEY INTEGRATION
    # ============================================
    ORANGE_MONEY_API_KEY: str = ""
    ORANGE_MONEY_API_SECRET: str = ""
    ORANGE_MONEY_MERCHANT_ID: str = ""
    ORANGE_MONEY_API_URL: str = "https://api.orange.com/orange-money"
    ORANGE_MONEY_CALLBACK_URL: str = ""
    
    # ============================================
    # MOOV MONEY INTEGRATION
    # ============================================
    MOOV_MONEY_API_KEY: str = ""
    MOOV_MONEY_API_SECRET: str = ""
    MOOV_MONEY_MERCHANT_ID: str = ""
    MOOV_MONEY_API_URL: str = "https://api.moovmoney.com"
    MOOV_MONEY_CALLBACK_URL: str = ""
    
    # ============================================
    # WAVE INTEGRATION
    # ============================================
    WAVE_API_KEY: str = ""
    WAVE_API_SECRET: str = ""
    WAVE_API_URL: str = "https://api.wavemoney.io"
    WAVE_CALLBACK_URL: str = ""
    
    # ============================================
    # BANK API INTEGRATION
    # ============================================
    BANK_API_KEY: str = ""
    BANK_API_URL: str = ""
    BANK_API_MERCHANT_ID: str = ""
    
    # ============================================
    # SMS & NOTIFICATIONS (Twilio)
    # ============================================
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = ""
    TWILIO_ENABLED: bool = False
    
    # ============================================
    # EMAIL CONFIGURATION
    # ============================================
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_FROM_EMAIL: str = "noreply@amchi.com"
    SMTP_FROM_NAME: str = "Amchi Payment Gateway"
    SMTP_ENABLED: bool = False
    
    # ============================================
    # REDIS CONFIGURATION
    # ============================================
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_DB: int = 0
    REDIS_PASSWORD: str = ""
    
    # ============================================
    # LOGGING CONFIGURATION
    # ============================================
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/amchi.log"
    LOG_FORMAT: str = "json"
    
    # ============================================
    # SECURITY & COMPLIANCE
    # ============================================
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = 60
    RATE_LIMIT_REQUESTS_PER_HOUR: int = 1000
    
    # ============================================
    # KYC & VERIFICATION
    # ============================================
    KYC_ENABLED: bool = True
    KYC_VERIFICATION_TIMEOUT_HOURS: int = 24
    MIN_TRANSACTION_AMOUNT: float = 100.0
    MAX_TRANSACTION_AMOUNT: float = 500000.0
    DAILY_LIMIT_AMOUNT: float = 2000000.0
    
    # ============================================
    # FEATURE FLAGS
    # ============================================
    ENABLE_P2P_TRANSFERS: bool = True
    ENABLE_MERCHANT_PAYMENTS: bool = True
    ENABLE_WITHDRAWAL: bool = True
    ENABLE_USSD: bool = True
    ENABLE_OFFLINE_MODE: bool = True
    
    # ============================================
    # AWS CONFIGURATION
    # ============================================
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET_NAME: str = "amchi-uploads"
    AWS_S3_REGION: str = "us-east-1"
    
    # ============================================
    # MONITORING & ANALYTICS
    # ============================================
    SENTRY_DSN: str = ""
    DATADOG_API_KEY: str = ""
    ENABLE_MONITORING: bool = False
    
    # ============================================
    # TIMEZONE
    # ============================================
    TIMEZONE: str = "Africa/Niamey"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create global settings instance
settings = Settings()