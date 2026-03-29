from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import text

# SQLAlchemy database engine configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Change to your database URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Base declarative class
Base = declarative_base()

# Session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to initialize the database
def init_db() -> None:
    Base.metadata.create_all(bind=engine)

# Function to drop all tables in the database
def drop_db() -> None:
    Base.metadata.drop_all(bind=engine)