from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone_number = Column(String)
    hashed_password = Column(String, nullable=False)
    public_key = Column(String)
    private_key = Column(String)
    encryption_phrase = Column(String)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    kyc_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def set_password(self, password):
        # Logic to hash and set the password
        self.hashed_password = hash_password(password)

    def verify_password(self, password):
        # Logic to verify the provided password
        return verify_hash(password, self.hashed_password)

    def generate_keys(self):
        # Logic to generate public and private keys
        self.public_key, self.private_key = generate_keys()
