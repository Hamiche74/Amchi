import bcrypt
import jwt
from datetime import datetime, timedelta
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class Auth:
    # Generate an RSA key pair
    @staticmethod
    def generate_keys():
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key, public_key

    # Hashing a password
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed

    # Verify a password
    @staticmethod
    def verify_password(stored_password, provided_password):
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

    # Create a JWT token
    @staticmethod
    def create_token(data, secret, exp_minutes=30):
        expiration = datetime.utcnow() + timedelta(minutes=exp_minutes)
        token = jwt.encode({'exp': expiration, **data}, secret, algorithm='HS256')
        return token

    # Decrypt the token with the private RSA key
    @staticmethod
    def decrypt_token(encrypted_token, private_key):
        rsa_key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        decrypted = cipher.decrypt(encrypted_token)
        return decrypted.decode('utf-8')

    # Encrypt data with the public RSA key
    @staticmethod
    def encrypt_data(data, public_key):
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted = cipher.encrypt(data.encode('utf-8'))
        return encrypted